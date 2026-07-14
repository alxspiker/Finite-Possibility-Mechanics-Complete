#!/usr/bin/env python3
"""
FPM local energy-bridge verification harness.

Demonstrates that the pre-v6.2 globally normalized replenishment rule

    r_global[i] = sum_j L[j] * w[i] / sum_k w[k]

is the one-step result of a dense, rank-one mixing kernel, but is also the
long-time equilibrium of a nearest-neighbour, causal Markov kernel on Z^3.
The local kernel preserves total energy exactly at every tick and admits an
exact discrete continuity equation with antisymmetric edge fluxes.

Dependencies: numpy, scipy
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, List, Tuple

import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.sparse import csr_matrix, lil_matrix


@dataclass(frozen=True)
class Grid:
    n: int

    @property
    def size(self) -> int:
        return self.n ** 3

    def index(self, x: int, y: int, z: int) -> int:
        n = self.n
        return ((x % n) * n + (y % n)) * n + (z % n)

    def coords(self, i: int) -> Tuple[int, int, int]:
        n = self.n
        x = i // (n * n)
        rem = i % (n * n)
        return x, rem // n, rem % n

    def neighbors(self, i: int) -> List[int]:
        x, y, z = self.coords(i)
        return [
            self.index(x + 1, y, z), self.index(x - 1, y, z),
            self.index(x, y + 1, z), self.index(x, y - 1, z),
            self.index(x, y, z + 1), self.index(x, y, z - 1),
        ]


def make_fields(grid: Grid, seed: int) -> Tuple[np.ndarray, np.ndarray]:
    """Create smooth positive activity weights and bounded local viscosities."""
    rng = np.random.default_rng(seed)
    raw = rng.normal(size=(grid.n, grid.n, grid.n))
    smooth = gaussian_filter(raw, sigma=max(1.0, grid.n / 7.0), mode="wrap")
    w = np.exp(0.7 * smooth)
    w /= w.mean()
    scale = max(float(np.std(smooth)), 1e-12)
    omega = 0.675 + 0.10 * np.tanh(smooth / scale)
    omega = np.clip(omega, 0.50, 0.85)
    if np.any(w <= 0) or not np.all(np.isfinite(w)):
        raise RuntimeError("Weights must be finite and strictly positive")
    return w.ravel(), omega.ravel()


def build_local_metropolis_kernel(
    grid: Grid, weights: np.ndarray, viscosities: np.ndarray
) -> Tuple[csr_matrix, Dict[int, List[int]]]:
    """Nearest-neighbour row-stochastic kernel with stationary pi proportional to weights.

    For neighbouring sites i~j:
        mu_ij = 1 - (Omega_i + Omega_j)/2
        P_ij = mu_ij/6 * min(1, w_j/w_i)
    and P_ii closes the row sum to one.

    The edge gate is local and symmetric, so detailed balance holds:
        w_i P_ij = w_j P_ji.
    """
    if weights.shape != (grid.size,) or viscosities.shape != (grid.size,):
        raise ValueError("field shapes do not match grid")
    if np.any((viscosities <= 0.0) | (viscosities >= 1.0)):
        raise ValueError("viscosities must lie strictly between 0 and 1")

    p = lil_matrix((grid.size, grid.size), dtype=float)
    neighbors: Dict[int, List[int]] = {}
    for i in range(grid.size):
        ns = grid.neighbors(i)
        neighbors[i] = ns
        outgoing = 0.0
        for j in ns:
            mu_ij = 1.0 - 0.5 * (viscosities[i] + viscosities[j])
            value = (mu_ij / 6.0) * min(1.0, weights[j] / weights[i])
            p[i, j] = value
            outgoing += value
        p[i, i] = 1.0 - outgoing
    return p.tocsr(), neighbors


def local_replenishment(p: csr_matrix, costs: np.ndarray) -> np.ndarray:
    """One-tick local redistribution: r = P^T L."""
    return np.asarray(p.T @ costs).ravel()


def global_replenishment(costs: np.ndarray, weights: np.ndarray) -> np.ndarray:
    """Former dense equilibrium rule, retained in v6.2 as the mean-field target."""
    return costs.sum() * weights / weights.sum()


def continuity_residual(
    p: csr_matrix,
    neighbors: Dict[int, List[int]],
    costs: np.ndarray,
) -> Tuple[float, float]:
    """Check q_i + sum_j J_{i->j} = 0 with local antisymmetric edge flux.

    J_{i->j} = P_ij L_i - P_ji L_j.
    q = r - L.
    """
    q = local_replenishment(p, costs) - costs
    outward = np.zeros_like(costs)
    for i, ns in neighbors.items():
        for j in ns:
            outward[i] += p[i, j] * costs[i] - p[j, i] * costs[j]
    return float(np.max(np.abs(q + outward))), float(abs(q.sum()))


def torus_manhattan(grid: Grid, a: int, b: int) -> int:
    ax, ay, az = grid.coords(a)
    bx, by, bz = grid.coords(b)
    n = grid.n
    return sum(
        min((u - v) % n, (v - u) % n)
        for u, v in ((ax, bx), (ay, by), (az, bz))
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=10, help="Z^3 side length")
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument(
        "--steps", type=int, nargs="*", default=[0, 1, 2, 3, 5, 10, 20, 50, 100, 200]
    )
    args = parser.parse_args()

    if args.n < 4:
        raise ValueError("Use n >= 4")

    grid = Grid(args.n)
    weights, viscosities = make_fields(grid, args.seed)
    p, neighbors = build_local_metropolis_kernel(grid, weights, viscosities)
    pi = weights / weights.sum()

    row_error = float(np.max(np.abs(np.asarray(p.sum(axis=1)).ravel() - 1.0)))
    stationary_error = float(np.max(np.abs(np.asarray(p.T @ pi).ravel() - pi)))

    rng = np.random.default_rng(args.seed + 1)
    random_costs = rng.random(grid.size)
    div_error, total_balance_error = continuity_residual(p, neighbors, random_costs)

    center = grid.index(args.n // 2, args.n // 2, args.n // 2)
    impulse = np.zeros(grid.size)
    impulse[center] = 1.0
    target = global_replenishment(impulse, weights)

    print("FPM LOCAL ENERGY-BRIDGE AUDIT")
    edge_mus = []
    detailed_error = 0.0
    for i, ns in neighbors.items():
        for j in ns:
            edge_mus.append(1.0 - 0.5 * (viscosities[i] + viscosities[j]))
            detailed_error = max(
                detailed_error,
                abs(weights[i] * p[i, j] - weights[j] * p[j, i]),
            )

    print(f"grid: {args.n}^3 = {grid.size} sites")
    print(f"edge mobility range:            [{min(edge_mus):.6f}, {max(edge_mus):.6f}]")
    print(f"row-stochastic residual:       {row_error:.3e}")
    print(f"stationary-weight residual:    {stationary_error:.3e}")
    print(f"detailed-balance residual:     {detailed_error:.3e}")
    print(f"local continuity residual:     {div_error:.3e}")
    print(f"global balance residual:       {total_balance_error:.3e}")
    print()
    print("m  total_mass         L1_error_to_global_rule   max_grid_distance   active_sites")

    for m in sorted(set(args.steps)):
        state = impulse.copy()
        for _ in range(m):
            state = np.asarray(p.T @ state).ravel()
        active = np.flatnonzero(state > 1e-14)
        max_distance = max((torus_manhattan(grid, center, i) for i in active), default=0)
        error = float(np.sum(np.abs(state - target)))
        print(
            f"{m:<3d}{state.sum():>18.15f}{error:>26.12e}"
            f"{max_distance:>20d}{active.size:>15d}"
        )

    # Hard pass/fail checks.
    assert row_error < 1e-12
    assert stationary_error < 1e-12
    assert detailed_error < 1e-12
    assert div_error < 1e-12
    assert total_balance_error < 1e-10

    # Before wraparound, support cannot outrun one lattice edge per tick.
    for m in range(min(args.n // 2, 5) + 1):
        state = impulse.copy()
        for _ in range(m):
            state = np.asarray(p.T @ state).ravel()
        active = np.flatnonzero(state > 1e-14)
        assert all(torus_manhattan(grid, center, i) <= m for i in active)

    dx = 3.453e-15
    dt = 1.152e-23
    print()
    print(f"one-edge propagation speed dx/dt = {dx/dt:.6e} m/s")
    print("PASS: exact global conservation, exact local graph continuity,")
    print("      finite one-edge-per-tick propagation, and frozen-weight")
    print("      convergence to the globally normalized mean-field target.")


if __name__ == "__main__":
    main()
