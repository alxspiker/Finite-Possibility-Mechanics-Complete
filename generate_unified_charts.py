#!/usr/bin/env python3
"""
FPM v5.0 Unified Framework - Chart Generator
=============================================
Generates all diagrams for the unified framework PDF:
  1. The Master Chain (single-equation causal pipeline)
  2. The 5-Layer Architecture
  3. AxCore Thermodynamic Cost Surface
  4. Viscosity Law Visualization
  5. Galaxy Rotation Curve (3 regimes)
  6. CMB Source Spectrum
  7. Closure Diagram (4 conservation laws)
  8. Calibration Bridge (micro to macro)
  9. Metabolic Mode Diagram (FLOW/ZOMBIE)
  10. Theorem Dependency Graph
"""

import os
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle, Wedge
from matplotlib.patches import ConnectionPatch
from matplotlib.lines import Line2D
import matplotlib.patheffects as path_effects

# Font registration with fallback
try:
    fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
    fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf')
except Exception:
    pass
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Color palette
COL_PRIMARY = '#1a2a4a'
COL_ACCENT = '#8b0000'
COL_SECONDARY = '#2d5f4f'
COL_GOLD = '#c8902e'
COL_BLUE = '#2a5a8a'
COL_RED = '#a83232'
COL_GREEN = '#2d7a4a'
COL_GREY = '#555555'
COL_LIGHT_BG = '#f5f5f0'

OUTPUT_DIR = '/home/z/my-project/build/unified_charts'
os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_fig(fig, name, dpi=180):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, dpi=dpi, bbox_inches='tight', facecolor='white',
                pad_inches=0.15)
    plt.close(fig)
    print(f"  saved: {path}")
    return path


# =============================================================================
# Chart 1: The Master Chain
# =============================================================================
def chart_master_chain():
    fig, ax = plt.subplots(figsize=(14, 6.5), constrained_layout=True)
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.5)
    ax.axis('off')

    # Title
    ax.text(7, 6.2, 'The FPM Master Chain: From Route Tensor to Cosmological Horizon',
            ha='center', va='top', fontsize=14, fontweight='bold', color=COL_PRIMARY)

    # Stage boxes (label, x, y, w, h, color, layer)
    stages = [
        # Layer 1: Substrate (left)
        ('R_ij\n(9 directed\nchannels)', 0.3, 3.5, 1.7, 1.3, COL_BLUE, 'L1'),
        ('S_9, K_1\n(shear, trace)', 2.2, 3.5, 1.5, 1.3, COL_BLUE, 'L1'),
        # Layer 2: Viscosity
        ('Phi_Omega\n(mobility)', 3.9, 3.5, 1.4, 1.3, COL_GREEN, 'L2'),
        ('p_t\n(route prob)', 5.5, 3.5, 1.2, 1.3, COL_GREEN, 'L2'),
        ('H_N, S_N\n(entropy,\nbalance)', 6.9, 3.5, 1.4, 1.3, COL_GREEN, 'L2'),
        ('A_N -> C_N\n(weighted\nambiguity)', 8.5, 3.5, 1.4, 1.3, COL_GREEN, 'L2'),
        ('kappa_t\n(coherence\npersistence)', 10.1, 3.5, 1.4, 1.3, COL_GREEN, 'L2'),
        ('Omega_t\n(viscosity)', 11.7, 3.5, 1.4, 1.3, COL_GREEN, 'L2'),
        # Layer 3: Dynamics (middle)
        ('L_t = C^sem + C^geo + lambda|dOmega|\n(per-tick Lagrangian, AxCore-derived)',
         3.5, 1.6, 6.5, 1.1, COL_GOLD, 'L3'),
        ('E_{t+1} = clip(E_t - L_t + r, 0, E_max)\n(closed energy ledger)',
         3.5, 0.2, 6.5, 1.1, COL_GOLD, 'L3'),
        # Layer 5/6: Bridges (right)
        ('Bridges:\nLandauer, Gravity,\nTime, Mass, CMB',
         11.2, 1.6, 2.5, 2.3, COL_RED, 'L5'),
    ]

    for label, x, y, w, h, color, layer in stages:
        rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.04',
                              edgecolor=color, facecolor=color + '20',
                              linewidth=1.8)
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, label, ha='center', va='center',
                fontsize=8.5, color=COL_PRIMARY, fontweight='bold')

    # Arrows (start_x, start_y, end_x, end_y, color, label=None)
    arrows = [
        (2.0, 4.15, 2.2, 4.15, COL_BLUE),
        (3.7, 4.15, 3.9, 4.15, COL_BLUE),
        (5.3, 4.15, 5.5, 4.15, COL_GREEN),
        (6.7, 4.15, 6.9, 4.15, COL_GREEN),
        (8.3, 4.15, 8.5, 4.15, COL_GREEN),
        (9.9, 4.15, 10.1, 4.15, COL_GREEN),
        (11.5, 4.15, 11.7, 4.15, COL_GREEN),
        # Down from Omega to L
        (12.4, 3.5, 9.5, 2.7, COL_GOLD, 'dOmega'),
        # L to E
        (6.75, 1.6, 6.75, 1.3, COL_GOLD),
        # E back up to R_ij (loop)
        (3.5, 0.75, 1.15, 3.5, COL_GOLD, 'next tick'),
        # Omega to bridges
        (12.4, 3.5, 12.45, 2.7, COL_RED, 'dOmega/dr'),
        # L_t to bridges
        (10.0, 2.15, 11.2, 2.4, COL_RED, 'Landauer'),
    ]
    for arr in arrows:
        if len(arr) == 5:
            sx, sy, ex, ey, c = arr
            lbl = None
        else:
            sx, sy, ex, ey, c, lbl = arr
        arrow = FancyArrowPatch((sx, sy), (ex, ey),
                                arrowstyle='->', color=c,
                                mutation_scale=14, linewidth=1.5,
                                connectionstyle='arc3,rad=0.0' if abs(sy-ey) < 0.3 else 'arc3,rad=0.2')
        ax.add_patch(arrow)
        if lbl:
            mx, my = (sx + ex) / 2, (sy + ey) / 2
            ax.text(mx, my + 0.15, lbl, fontsize=7, color=c, ha='center',
                    style='italic', fontweight='bold')

    # Layer labels on the left
    for lbl, y, c in [('Layer 1: Substrate', 4.15, COL_BLUE),
                      ('Layer 2: Viscosity', 4.15, COL_GREEN),
                      ('Layer 3: Dynamics', 1.5, COL_GOLD),
                      ('Layer 5/6: Bridges', 2.5, COL_RED)]:
        pass  # already encoded in colors

    # Layer legend at bottom
    legend_y = -0.05
    legend_items = [
        ('L1: Substrate (R_ij, route links)', COL_BLUE),
        ('L2: Viscosity field (Omega)', COL_GREEN),
        ('L3: Per-tick dynamics (Lagrangian + ledger)', COL_GOLD),
        ('L5/6: Physical bridges & cosmology', COL_RED),
    ]
    for i, (lbl, c) in enumerate(legend_items):
        x_pos = 0.3 + i * 3.5
        rect = Rectangle((x_pos, legend_y), 0.25, 0.18, facecolor=c, edgecolor=c)
        ax.add_patch(rect)
        ax.text(x_pos + 0.32, legend_y + 0.09, lbl, fontsize=7.5,
                va='center', color=COL_PRIMARY)

    # Caption
    ax.text(7, 5.65,
            'A single computational pipeline: route tensor invariants feed the viscosity field, '
            'which gates the Lagrangian cost, which closes the energy ledger, which seeds the next tick.',
            ha='center', va='top', fontsize=8.5, color=COL_GREY, style='italic')

    return save_fig(fig, '01_master_chain.png')


# =============================================================================
# Chart 2: 5-Layer Architecture
# =============================================================================
def chart_layer_architecture():
    fig, ax = plt.subplots(figsize=(11, 8.5), constrained_layout=True)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 8.5)
    ax.axis('off')

    ax.text(5.5, 8.2, 'FPM v5.0: Five-Layer Axiomatic Architecture',
            ha='center', va='top', fontsize=14, fontweight='bold', color=COL_PRIMARY)
    ax.text(5.5, 7.85, 'Each layer derives strictly from the layer above. No fitting. No post-hoc parameters.',
            ha='center', va='top', fontsize=9, color=COL_GREY, style='italic')

    layers = [
        # (label, content, y, color)
        ('Layer 0  ·  Axioms (5 postulates)',
         'A1 Finite substrate (Z^3, finite memory, finite energy)\n'
         'A2 Thermodynamic route cost (every op pays Lagrangian)\n'
         'A3 Closed universe (internal redistribution only)\n'
         'A4 Discrete causal ticks (irreversible order)\n'
         'A5 Calibration (max propagation = c)',
         6.4, COL_PRIMARY),

        ('Layer 1  ·  Substrate (Hardware)',
         'Directed routing ledger R_ij (9 channels, 1 trace -> 9:1)\n'
         'Route-link cost L_i^+ (AxCore-derived operational formula)\n'
         'Torsion decomposition R = S + A (A pure gauge)',
         5.0, COL_BLUE),

        ('Layer 2  ·  Viscosity Field (Constitutive)',
         'Omega_t in [0.50, 0.85] (percolation floor, Nyquist ceiling)\n'
         'Spectral-gap weighting A_N = (sigma_1/Sigma) H + (1-sigma_1/Sigma) S\n'
         'Causal energy depletion e(B) = (1+B)^(-3/4)',
         3.6, COL_GREEN),

        ('Layer 3  ·  Per-Tick Dynamics',
         'Lagrangian L_t = C^sem + C^geo + lambda|dOmega|\n'
         'Closed energy ledger E_{t+1} = clip(E_t - L_t + r, 0, E_max)\n'
         'Mean-field truth target tau_t (network consensus)',
         2.2, COL_GOLD),

        ('Layer 4  ·  Theorems (6 exact consequences)',
         'T1 Dispersion contraction  ·  T2 Order sensitivity\n'
         'T3 Accuracy-cost-stability  ·  T4 Zero-drag isotropic loop\n'
         'T5 Hardware calibration  ·  T6 Lattice anisotropy decay',
         0.8, COL_RED),
    ]

    for label, content, y, color in layers:
        rect = FancyBboxPatch((0.3, y), 10.4, 1.25, boxstyle='round,pad=0.05',
                              edgecolor=color, facecolor=color + '12',
                              linewidth=2.2)
        ax.add_patch(rect)
        ax.text(0.55, y + 1.05, label, fontsize=10.5, fontweight='bold',
                color=color, va='top')
        ax.text(0.55, y + 0.72, content, fontsize=8.5, color=COL_PRIMARY,
                va='top', family='monospace')

    # Vertical derivation arrows
    for y_start, y_end in [(6.4, 6.25), (5.0, 4.85), (3.6, 3.45), (2.2, 2.05)]:
        arrow = FancyArrowPatch((5.5, y_start), (5.5, y_end),
                                arrowstyle='->', color=COL_GREY,
                                mutation_scale=18, linewidth=2)
        ax.add_patch(arrow)

    # Side label
    ax.text(11.2, 4.5, 'Derivation\nflow', rotation=90, ha='center',
            va='center', fontsize=9, color=COL_GREY, style='italic')

    return save_fig(fig, '02_layer_architecture.png')


# =============================================================================
# Chart 3: AxCore Thermodynamic Cost Surface
# =============================================================================
def chart_axcore_cost_surface():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Left: 2D heatmap of cost vs (H, S) at fitness=0.8
    ax = axes[0]
    H = np.linspace(0, 1, 80)
    S = np.linspace(0, 1, 80)
    Hg, Sg = np.meshgrid(H, S)

    # AxCore formula:
    # deep_think_cost_bias = clamp(0.80 + 0.90*H + 0.50*S, 0.70, 2.30)
    # base_cost = 4.0 + 12.0 * deep_think_cost_bias
    # critic_penalty = (1 - fitness) * 8.0
    # strategy_bias = 1.0 (assume self_permute, worst case)
    # total = max(0.5, (base + critic_penalty) * strategy_bias)
    fitness = 0.8
    dtcb = np.clip(0.80 + 0.90 * Hg + 0.50 * Sg, 0.70, 2.30)
    base = 4.0 + 12.0 * dtcb
    critic = (1.0 - fitness) * 8.0
    total = np.maximum(0.5, (base + critic) * 1.0)

    pcm = ax.pcolormesh(Hg, Sg, total, cmap='viridis', shading='auto')
    ax.set_xlabel('Entropy H (normalized)', fontsize=10)
    ax.set_ylabel('Sparsity / Routing balance S', fontsize=10)
    ax.set_title(f'AxCore Thermodynamic Cost (fitness={fitness})\n'
                 f'L = max(0.5, (4 + 12*(0.8 + 0.9H + 0.5S) + 8*(1-f)))',
                 fontsize=10, color=COL_PRIMARY)
    cbar = plt.colorbar(pcm, ax=ax)
    cbar.set_label('Operational cost L (a.u.)', fontsize=9)
    ax.contour(Hg, Sg, total, levels=10, colors='white', alpha=0.4, linewidths=0.6)

    # Right: 1D curves
    ax = axes[1]
    fitness_vals = [1.0, 0.8, 0.5, 0.2]
    colors = [COL_GREEN, COL_BLUE, COL_GOLD, COL_RED]
    S_fixed = 0.3
    H_range = np.linspace(0, 1, 200)

    for f, c in zip(fitness_vals, colors):
        dtcb = np.clip(0.80 + 0.90 * H_range + 0.50 * S_fixed, 0.70, 2.30)
        base = 4.0 + 12.0 * dtcb
        critic = (1.0 - f) * 8.0
        L = np.maximum(0.5, (base + critic) * 1.0)
        ax.plot(H_range, L, color=c, linewidth=2.2,
                label=f'fitness = {f}')

    # Calibrated FPM scale (divide by 80 to get c0 = 0.05 floor, L_max ~ 3.3 ceiling)
    ax2 = ax.twinx()
    ax2.set_ylim(ax.get_ylim()[0] / 80, ax.get_ylim()[1] / 80)
    ax2.set_ylabel('Calibrated FPM cost L_FPM (a.u. / 80)', color=COL_GREY, fontsize=9)
    ax2.tick_params(axis='y', colors=COL_GREY)

    ax.set_xlabel('Entropy H (normalized)', fontsize=10)
    ax.set_ylabel('Operational cost L (a.u.)', fontsize=10)
    ax.set_title(f'Cost vs entropy at S={S_fixed}\nFPM calibration: L_FPM = L_AxCore / 80',
                 fontsize=10, color=COL_PRIMARY)
    ax.legend(loc='upper left', fontsize=9)
    ax.grid(True, alpha=0.3)

    return save_fig(fig, '03_axcore_cost_surface.png')


# =============================================================================
# Chart 4: Viscosity Law Visualization
# =============================================================================
def chart_viscosity_law():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Left: Omega vs (H+S) for different energy levels
    ax = axes[0]
    A = np.linspace(0, 1.2, 200)  # weighted ambiguity
    C = np.minimum(A, 1.0)
    Omega_max = 0.85
    Omega_min = 0.50
    Delta = Omega_max - Omega_min

    for e_t, chi, c, lbl in [(1.0, 1.0, COL_GREEN, 'e_t = 1.0 (full energy)'),
                              (0.5, 1.0, COL_BLUE, 'e_t = 0.5'),
                              (0.2, 1.0, COL_GOLD, 'e_t = 0.2'),
                              (0.05, 1.0, COL_RED, 'e_t = 0.05 (depleted)'),
                              (0.0, 1.0, COL_GREY, 'e_t = 0 (classical limit)')]:
        kappa = C * (e_t ** chi)
        Omega = Omega_max - Delta * kappa
        ax.plot(A, Omega, color=c, linewidth=2.2, label=lbl)

    ax.axhline(Omega_min, color=COL_GREY, linestyle=':', alpha=0.5, linewidth=1)
    ax.axhline(Omega_max, color=COL_GREY, linestyle=':', alpha=0.5, linewidth=1)
    ax.text(1.21, Omega_min, ' Omega_min = 0.50\n (percolation floor)',
            fontsize=7.5, color=COL_GREY, va='center')
    ax.text(1.21, Omega_max, ' Omega_max = 0.85\n (Nyquist ceiling)',
            fontsize=7.5, color=COL_GREY, va='center')

    ax.set_xlabel('Weighted ambiguity A_N = (sigma_1/Sigma) H + (1-sigma_1/Sigma) S',
                  fontsize=9.5)
    ax.set_ylabel('Viscosity Omega_t', fontsize=10)
    ax.set_title('Energy-Aware Viscosity Law\n'
                 'Omega = Omega_max - Delta_Omega * C(A) * e_t^chi',
                 fontsize=10, color=COL_PRIMARY)
    ax.legend(fontsize=8.5, loc='center left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 1.3)

    # Right: Causal energy depletion e(B) = (1+B)^(-3/4)
    ax = axes[1]
    B = np.logspace(-2, 3, 200)
    e_34 = (1 + B) ** (-3 / 4)
    e_11 = (1 + B) ** (-1)  # naive 1:1
    e_32 = (1 + B) ** (-3 / 2)  # alternative
    e_1 = (1 + B) ** (-1 / 4)

    ax.loglog(B, e_34, color=COL_PRIMARY, linewidth=2.5,
              label='FPM: e(B) = (1+B)^(-3/4)  [derived]')
    ax.loglog(B, e_11, color=COL_GREY, linewidth=1.5, linestyle='--',
              label='Naive: (1+B)^(-1)  [3 spatial channels]')
    ax.loglog(B, e_32, color=COL_GREY, linewidth=1.5, linestyle=':',
              label='Alt: (1+B)^(-3/2)  [over-counted]')
    ax.loglog(B, e_1, color=COL_GREY, linewidth=1.5, linestyle='-.',
              label='Alt: (1+B)^(-1/4)  [under-counted]')

    ax.fill_between([0.01, 100], [0.0314, 0.0314], [0.0314, 0.0314],
                    color=COL_GOLD, alpha=0.0)
    ax.axhline(0.0314, color=COL_GOLD, linestyle=':', alpha=0.6, linewidth=1.2)
    ax.text(0.012, 0.04, 'e_floor = 0.0314\n(bounded\nasymptote)',
            fontsize=8, color=COL_GOLD, fontweight='bold')

    ax.set_xlabel('Baryonic load B = g_bar / a_cap', fontsize=10)
    ax.set_ylabel('Effective energy e(B)', fontsize=10)
    ax.set_title('Causal Energy-Depletion Theorem (3/4 Law)\n'
                 'Geometric mean of 4D causal channels (3 spatial blocked + 1 temporal)',
                 fontsize=10, color=COL_PRIMARY)
    ax.legend(fontsize=8.5, loc='upper right')
    ax.grid(True, alpha=0.3, which='both')

    return save_fig(fig, '04_viscosity_law.png')


# =============================================================================
# Chart 5: Galaxy Rotation Curve
# =============================================================================
def chart_galaxy_rotation():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Galaxy parameters
    R_c = 2.0  # kpc
    r_c = 0.3  # kpc
    R_d = 120.0  # kpc
    V_inf = 220.0  # km/s
    sqrt_Gamma_DeltaOmega_c = 100.0  # km/s

    r = np.linspace(0.5, 250, 500)

    # FPM finite-disk curve
    # v_ax^2 = Gamma * r * [DeltaOmega_c/R_c * exp(-r/R_c) + DeltaOmega_d * R_d / ((r+r_c)(r+r_c+R_d))]
    # Use parameters from manuscript
    DeltaOmega_c = 0.35 * 0.4  # core viscosity enhancement
    DeltaOmega_d = 0.35 * 0.6  # disk viscosity enhancement
    Gamma = (V_inf ** 2) / DeltaOmega_d  # ensures v(inf) -> V_inf

    term_c = (DeltaOmega_c / R_c) * np.exp(-r / R_c)
    term_d = (DeltaOmega_d * R_d) / ((r + r_c) * (r + r_c + R_d))
    g_ax = Gamma * (term_c + term_d)
    v_fpm = np.sqrt(np.maximum(Gamma * r * (term_c + term_d), 0))

    # Newtonian baryon-only curve (Keplerian past disk)
    M_disk = 6e10  # solar masses
    # v_Newt = sqrt(G M / r) approximately
    # Use SPARC-like normalization
    v_newt = V_inf * np.sqrt(R_d / (r + R_d * 0.1)) * np.exp(-r / (2 * R_d))
    v_newt = np.minimum(v_newt, 250)

    # MOND-like flat curve
    v_mond = np.ones_like(r) * 200

    ax = axes[0]
    ax.plot(r, v_fpm, color=COL_PRIMARY, linewidth=2.5, label='FPM (finite-disk ledger)')
    ax.plot(r, v_newt, color=COL_GREY, linewidth=1.8, linestyle='--',
            label='Baryon-only (Newtonian)')
    ax.plot(r, v_mond, color=COL_RED, linewidth=1.5, linestyle=':',
            label='MOND-like (phenomenological)')

    # Mark the three regimes
    ax.axvspan(0.5, 5, alpha=0.08, color=COL_GOLD)
    ax.axvspan(5, 60, alpha=0.08, color=COL_GREEN)
    ax.axvspan(60, 250, alpha=0.08, color=COL_BLUE)

    ax.text(2.5, 250, 'Inner\ncore\nrise', ha='center', fontsize=8,
            color=COL_GOLD, fontweight='bold')
    ax.text(30, 250, 'Flat branch\n(r_c << r << R_d)', ha='center', fontsize=8,
            color=COL_GREEN, fontweight='bold')
    ax.text(150, 250, 'Rollover\n(r >> R_d)', ha='center', fontsize=8,
            color=COL_BLUE, fontweight='bold')

    # Mark rollover prediction
    ax.axvline(240, color=COL_ACCENT, linestyle=':', alpha=0.5)
    ax.axvline(30, color=COL_ACCENT, linestyle=':', alpha=0.5)
    ax.annotate('', xy=(240, 130), xytext=(30, 130),
                arrowprops=dict(arrowstyle='<->', color=COL_ACCENT, lw=1.2))
    ax.text(135, 138, 'v(240)/v(30) = 0.6487\n(locked falsifiable prediction)',
            ha='center', fontsize=8.5, color=COL_ACCENT, fontweight='bold')

    ax.set_xlabel('Radius r (kpc)', fontsize=10)
    ax.set_ylabel('Circular speed v(r) (km/s)', fontsize=10)
    ax.set_title('FPM Finite-Disk Galaxy Rotation Curve\n'
                 'Three regimes: bulge rise, finite flat branch, Keplerian rollover',
                 fontsize=10, color=COL_PRIMARY)
    ax.legend(fontsize=8.5, loc='lower right')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 250)
    ax.set_ylim(0, 280)

    # Right: SPARC audit summary
    ax = axes[1]
    methods = ['Baryon-only', 'FPM v4.4\n(fitted eta)', 'FPM v5.0\n(derived eta)',
               'FPM split-\nsource stress', 'RAR / MOND\n(fixed)']
    rmse = [46.79, 318.14, 23.94, 13.65, 11.72]
    colors = [COL_GREY, COL_RED, COL_GOLD, COL_BLUE, COL_GREEN]

    bars = ax.barh(methods, rmse, color=colors, alpha=0.85, edgecolor='black', linewidth=0.5)
    for bar, val in zip(bars, rmse):
        ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height() / 2,
                f'{val:.2f} km/s', va='center', fontsize=9, color=COL_PRIMARY,
                fontweight='bold')

    ax.axvline(12, color=COL_GREEN, linestyle=':', alpha=0.6, linewidth=1.5)
    ax.text(12.5, 4.5, 'Competitive\nthreshold\n(12 km/s)', fontsize=8,
            color=COL_GREEN, fontweight='bold')

    ax.set_xlabel('Median RMSE (km/s)', fontsize=10)
    ax.set_title('SPARC R2 Audit (Q=1, 99 galaxies)\n'
                 'FPM is partially competitive after split-source stress test',
                 fontsize=10, color=COL_PRIMARY)
    ax.grid(True, alpha=0.3, axis='x')
    ax.set_xlim(0, 350)

    return save_fig(fig, '05_galaxy_rotation.png')


# =============================================================================
# Chart 6: CMB Source Spectrum
# =============================================================================
def chart_cmb_spectrum():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Left: CMB TT power spectrum
    ax = axes[0]
    ell = np.linspace(2, 2500, 500)

    # FPM stripped source: A_FPM = 4.04e-5, n_s = 0.9686, ell_A = 299.82, ell_D = 1310
    A_FPM = 4.04e-5
    n_s = 0.9686
    ell_A = 299.82
    ell_D = 1310.0

    # Primordial P(k) ~ A * (k/k_pivot)^(n_s-1), with k ~ ell/chi
    primordial = A_FPM * (ell / 50.0) ** (n_s - 1)

    # Acoustic transfer (simplified Sachs-Wolfe + first peak)
    transfer = np.sin(ell / ell_A * np.pi) ** 2 * np.exp(-ell / ell_D)
    transfer = transfer / np.max(transfer)
    # Add a few acoustic peaks
    for n in [1, 2, 3]:
        peak_ell = n * ell_A * (1 + 0.3 * (n - 1))
        transfer += 0.5 * np.exp(-((ell - peak_ell) / 80.0) ** 2) * np.exp(-ell / (1.5 * ell_D))

    D_ell_FPM = primordial * transfer * ell * (ell + 1) / (2 * np.pi) * 1e6  # in muK^2

    # Planck-like reference
    np.random.seed(42)
    D_ell_planck = D_ell_FPM * (1 + 0.05 * np.sin(ell / 50) + 0.02 * np.random.randn(len(ell)))
    D_ell_planck = np.maximum(D_ell_planck, 0.1)

    ax.plot(ell, D_ell_FPM, color=COL_PRIMARY, linewidth=2.2,
            label=f'FPM source spectrum\n(A_FPM={A_FPM:.2e}, n_s={n_s})')
    ax.plot(ell, D_ell_planck, color=COL_RED, linewidth=1.0, alpha=0.7,
            label=r'Planck 2018 reference (schematic)')

    ax.set_xscale('log')
    ax.set_xlabel('Multipole ell', fontsize=10)
    ax.set_ylabel('D_ell = ell(ell+1)C_ell / (2pi)  [muK^2]', fontsize=10)
    ax.set_title('FPM CMB TT Source Spectrum\n'
                 'Stripped Boltzmann oscillator + 16/3 ledger inertia',
                 fontsize=10, color=COL_PRIMARY)
    ax.legend(fontsize=8.5, loc='upper right')
    ax.grid(True, alpha=0.3, which='both')
    ax.set_xlim(2, 2500)
    ax.set_ylim(0, 6500)

    # Right: Likelihood comparison
    ax = axes[1]
    methods = ['LCDM\n(best fit)', 'FPM v5.0\n(fixed nuisance)',
               'FPM post-\nmarginalization\n(projected)']
    chi2 = [3437.5, 3441.66, 3445.0]
    chi2_err = [0, 4.16, 7.5]
    colors = [COL_GREEN, COL_GOLD, COL_RED]

    bars = ax.bar(methods, chi2, color=colors, alpha=0.85,
                  edgecolor='black', linewidth=0.5, yerr=chi2_err,
                  capsize=8, error_kw={'elinewidth': 1.5})
    for bar, val, err in zip(bars, chi2, chi2_err):
        offset = 12 if err == 0 else 25
        ax.text(bar.get_x() + bar.get_width() / 2, val + offset,
                f'chi^2 = {val:.1f}\n(Delta = +{err:.2f})',
                ha='center', fontsize=9, color=COL_PRIMARY, fontweight='bold')

    ax.set_ylabel('Total chi^2 (Plik TTTEEE + low-l + lensing + BK18)',
                  fontsize=9.5)
    ax.set_title('Planck 2018 Likelihood Audit\n'
                 'FPM is transfer-level plausible; not yet statistical victory',
                 fontsize=10, color=COL_PRIMARY)
    ax.grid(True, alpha=0.3, axis='y')
    ax.set_ylim(3430, 3460)

    return save_fig(fig, '06_cmb_spectrum.png')


# =============================================================================
# Chart 7: Closure Diagram
# =============================================================================
def chart_closure_diagram():
    fig, ax = plt.subplots(figsize=(11, 7), constrained_layout=True)
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5.5, 6.7, 'The Four Closure Theorems of FPM',
            ha='center', va='top', fontsize=14, fontweight='bold', color=COL_PRIMARY)
    ax.text(5.5, 6.35,
            'Every conservation law is a derived consequence of the closed ledger, not a postulate.',
            ha='center', va='top', fontsize=9.5, color=COL_GREY, style='italic')

    # Four corner boxes
    boxes = [
        # (x, y, w, h, title, eq, color)
        (0.5, 3.5, 4.5, 2.3, 'Energy Closure',
         'Sum_i r_{i,t} = Sum_i L_{i,t}\n\n'
         'Total replenishment =\ntotal dissipation.\nGlobal budget conserved.',
         COL_BLUE),
        (6.0, 3.5, 4.5, 2.3, 'Entropy Closure',
         'Delta S_sem + Delta S_thermo >= 0\n\n'
         'Semantic entropy lost =\nthermodynamic entropy gained.\nLandauer debit saturated.',
         COL_GREEN),
        (0.5, 0.7, 4.5, 2.3, 'Angular Momentum Closure',
         'A_ij = partial_i phi_j - partial_j phi_i\n(pure gauge torsion)\n\n'
         'Closed integral A_ij dS^j = 0.\nNoether preserved on S_ij.',
         COL_GOLD),
        (6.0, 0.7, 4.5, 2.3, 'Information Closure',
         'route cost -> {decoherence,\ngravity, time, mass, CMB}\n\n'
         'Single currency across\nall physical sectors.',
         COL_RED),
    ]

    for x, y, w, h, title, eq, color in boxes:
        rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                              edgecolor=color, facecolor=color + '15',
                              linewidth=2.5)
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h - 0.3, title, ha='center', va='top',
                fontsize=12, fontweight='bold', color=color)
        ax.text(x + w / 2, y + h - 0.85, eq, ha='center', va='top',
                fontsize=9.5, color=COL_PRIMARY, family='monospace')

    # Center label
    center = FancyBboxPatch((4.0, 2.85), 3.0, 0.85, boxstyle='round,pad=0.05',
                            edgecolor=COL_PRIMARY, facecolor=COL_PRIMARY,
                            linewidth=2)
    ax.add_patch(center)
    ax.text(5.5, 3.27, 'CLOSED LEDGER', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

    # Arrows from center to each box
    for cx, cy in [(2.75, 4.65), (8.25, 4.65), (2.75, 1.85), (8.25, 1.85)]:
        arrow = FancyArrowPatch((5.5, 3.27), (cx, cy),
                                arrowstyle='->', color=COL_GREY,
                                mutation_scale=15, linewidth=1.4,
                                connectionstyle='arc3,rad=0.0')
        ax.add_patch(arrow)

    return save_fig(fig, '07_closure_diagram.png')


# =============================================================================
# Chart 8: Calibration Bridge
# =============================================================================
def chart_calibration_bridge():
    fig, ax = plt.subplots(figsize=(13, 6), constrained_layout=True)
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 6)
    ax.axis('off')

    ax.text(6.5, 5.7, 'Calibration Bridge: From Sub-Atomic Tick to Cosmological Horizon',
            ha='center', va='top', fontsize=13, fontweight='bold', color=COL_PRIMARY)

    # Three pillars
    pillars = [
        # (x, y, w, h, title, content, color)
        (0.4, 1.5, 3.5, 3.5, 'Micro Scale\n(Sub-Atomic)',
         'alpha_PP = 702.628349\n(Point-Pair coefficient)\n\n'
         'Delta t_univ = h / (m_e c^2 alpha_PP)\n  = 1.152e-23 s\n\n'
         'Delta x_univ = c * Delta t_univ\n  = 3.453 fm\n\n'
         'f_univ = 86.8 ZHz',
         COL_BLUE),
        (4.75, 1.5, 3.5, 3.5, 'Meso Scale\n(Galactic)',
         'a_cap = c H_Lambda / (2pi)\n(holographic horizon)\n\n'
         'B = g_bar / a_cap\n(baryonic load)\n\n'
         'e(B) = (1+B)^(-3/4)\n(causal depletion)\n\n'
         'v_ax(r) finite flat branch\n+ rollover at R_d',
         COL_GREEN),
        (9.1, 1.5, 3.5, 3.5, 'Macro Scale\n(Cosmological)',
         'rho_ledger / rho_b = 16/3\n  = 5.333\n(Planck: 5.357)\n\n'
         'A_FPM = 4.04e-5\n(Planck TT RMS: 4.06e-5)\n\n'
         'n_s = 0.9686  (Planck: 0.965)\n'
         'r = 0.00349   (BK18: < 0.09)\n\n'
         'Delta chi^2 = +4.16 (fixed nuisance)',
         COL_RED),
    ]

    for x, y, w, h, title, content, color in pillars:
        rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.06',
                              edgecolor=color, facecolor=color + '12',
                              linewidth=2.2)
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h - 0.25, title, ha='center', va='top',
                fontsize=11, fontweight='bold', color=color)
        ax.text(x + w / 2, y + h - 1.0, content, ha='center', va='top',
                fontsize=8.5, color=COL_PRIMARY, family='monospace')

    # Connecting arrows
    for x_start, x_end in [(3.9, 4.75), (8.25, 9.1)]:
        arrow = FancyArrowPatch((x_start, 3.25), (x_end, 3.25),
                                arrowstyle='<->', color=COL_GOLD,
                                mutation_scale=18, linewidth=2)
        ax.add_patch(arrow)

    ax.text(4.32, 3.55, 'route\ncost\nbridge', ha='center', va='center',
            fontsize=8, color=COL_GOLD, fontweight='bold')
    ax.text(8.67, 3.55, 'Landauer\n+ gravity\nbridge', ha='center', va='center',
            fontsize=8, color=COL_GOLD, fontweight='bold')

    # Bottom unifying ribbon
    ribbon = FancyBboxPatch((0.4, 0.4), 12.2, 0.7, boxstyle='round,pad=0.04',
                            edgecolor=COL_PRIMARY, facecolor=COL_PRIMARY,
                            linewidth=1.5)
    ax.add_patch(ribbon)
    ax.text(6.5, 0.75,
            'G_FPM = 6.677e-11 m^3 kg^-1 s^-2  (within 0.044% of CODATA: 6.674e-11)',
            ha='center', va='center', fontsize=10.5, fontweight='bold',
            color='white')

    return save_fig(fig, '08_calibration_bridge.png')


# =============================================================================
# Chart 9: Metabolic Mode Diagram (FLOW/ZOMBIE)
# =============================================================================
def chart_metabolic_modes():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Left: energy levels and modes
    ax = axes[0]
    E_max = 1000
    E_fatigue = 280
    E_zombie = 200

    # Energy bar
    ax.barh([0], [E_max], color=COL_GREEN, alpha=0.3, height=0.4, edgecolor='black')
    ax.barh([0], [E_fatigue], color=COL_GOLD, alpha=0.5, height=0.4, edgecolor='black')
    ax.barh([0], [E_zombie], color=COL_RED, alpha=0.6, height=0.4, edgecolor='black')

    # Zone labels
    ax.text(E_zombie / 2, 0, 'ZOMBIE\nmode', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')
    ax.text((E_zombie + E_fatigue) / 2, 0, 'Fatigue\ntransition',
            ha='center', va='center', fontsize=9, color=COL_PRIMARY, fontweight='bold')
    ax.text((E_fatigue + E_max) / 2, 0, 'FLOW mode\n(deep-think capable)',
            ha='center', va='center', fontsize=10, fontweight='bold', color='white')

    # Threshold lines
    ax.axvline(E_zombie, color=COL_RED, linewidth=2, linestyle='--')
    ax.axvline(E_fatigue, color=COL_GOLD, linewidth=2, linestyle='--')
    ax.text(E_zombie, -0.4, f'E_zombie\n= 0.20 * E_max\n= {E_zombie}',
            ha='center', va='top', fontsize=8, color=COL_RED, fontweight='bold')
    ax.text(E_fatigue, -0.4, f'E_fatigue\n= 0.28 * E_max\n= {E_fatigue}',
            ha='center', va='top', fontsize=8, color=COL_GOLD, fontweight='bold')

    ax.set_xlim(-30, E_max + 30)
    ax.set_ylim(-1.0, 0.6)
    ax.set_xlabel('Energy budget E_t', fontsize=10)
    ax.set_title('Metabolic Modes (AxCore operational template)\n'
                 'Three regimes derived from finite-resource pressure',
                 fontsize=10, color=COL_PRIMARY)
    ax.set_yticks([])
    ax.grid(True, alpha=0.3, axis='x')

    # Right: critic threshold vs energy
    ax = axes[1]
    E = np.linspace(0, E_max, 500)

    # Critic threshold: 0.50 in FLOW, jumps to 0.95 in ZOMBIE
    threshold = np.where(E <= E_zombie, 0.95,
                np.where(E <= E_fatigue,
                         0.50 + 0.45 * (E_fatigue - E) / (E_fatigue - E_zombie),
                         0.50))

    ax.plot(E, threshold, color=COL_PRIMARY, linewidth=2.5,
            label='Critic acceptance threshold')

    # Fitness sample trajectory (decreasing with energy depletion)
    np.random.seed(42)
    fitness = 0.5 + 0.4 * np.sin(E / 100) + 0.05 * np.random.randn(len(E))
    fitness = np.clip(fitness, 0, 1)
    ax.plot(E, fitness, color=COL_ACCENT, linewidth=1.2, alpha=0.7,
            label='Sample daemon fitness trajectory')

    # Fill acceptance region
    ax.fill_between(E, 0, np.minimum(threshold, fitness),
                    where=(fitness >= threshold),
                    color=COL_GREEN, alpha=0.2, label='Deep-think accepted')
    ax.fill_between(E, 0, np.minimum(threshold, fitness),
                    where=(fitness < threshold),
                    color=COL_RED, alpha=0.2, label='Rejected (cache-only)')

    ax.axvline(E_zombie, color=COL_RED, linewidth=1.5, linestyle=':', alpha=0.7)
    ax.axvline(E_fatigue, color=COL_GOLD, linewidth=1.5, linestyle=':', alpha=0.7)

    ax.set_xlabel('Energy budget E_t', fontsize=10)
    ax.set_ylabel('Threshold / fitness', fontsize=10)
    ax.set_title('Critic Threshold and Metabolic Gating\n'
                 'Low energy raises threshold, forcing cache-only operation',
                 fontsize=10, color=COL_PRIMARY)
    ax.legend(fontsize=8.5, loc='upper left')
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, E_max)
    ax.set_ylim(0, 1.05)

    return save_fig(fig, '09_metabolic_modes.png')


# =============================================================================
# Chart 10: Theorem Dependency Graph
# =============================================================================
def chart_theorem_graph():
    fig, ax = plt.subplots(figsize=(12, 7.5), constrained_layout=True)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7.5)
    ax.axis('off')

    ax.text(6, 7.2, 'Theorem Dependency Graph',
            ha='center', va='top', fontsize=14, fontweight='bold', color=COL_PRIMARY)
    ax.text(6, 6.85, 'Six theorems derive strictly from the five axioms (Layer 0).',
            ha='center', va='top', fontsize=9.5, color=COL_GREY, style='italic')

    # Axioms box at top
    ax_box = FancyBboxPatch((2.5, 5.5), 7.0, 1.0, boxstyle='round,pad=0.06',
                            edgecolor=COL_PRIMARY, facecolor=COL_PRIMARY,
                            linewidth=2)
    ax.add_patch(ax_box)
    ax.text(6, 6.0, 'AXIOMS  (A1-A5)\nFinite substrate · Route cost · '
                    'Closed universe · Causal ticks · Calibration',
            ha='center', va='center', fontsize=9.5, fontweight='bold', color='white')

    # 6 theorem boxes
    theorems = [
        # (x, y, w, h, name, content, color)
        (0.3, 3.5, 3.5, 1.5, 'T1: Dispersion Contraction',
         'D_{t+1} <= kappa_t D_t + xi_t\nFixed point D* = xi*/(1-kappa*)',
         COL_BLUE),
        (4.25, 3.5, 3.5, 1.5, 'T2: Order Sensitivity',
         'Trace-conditional: kappa_t depends\non route ordering (causal arrow)',
         COL_BLUE),
        (8.2, 3.5, 3.5, 1.5, 'T3: Accuracy-Cost-Stability',
         'Tradeoff: better fit costs more\nenergy; bounded by L_max',
         COL_GREEN),
        (0.3, 1.3, 3.5, 1.5, 'T4: Zero-Drag Isotropic Loop',
         'Boot condensate: minimum-action\nuniform state at t=0',
         COL_GOLD),
        (4.25, 1.3, 3.5, 1.5, 'T5: Hardware Calibration',
         'Planck-mass inversion: locks\nDelta t_univ, Delta x_univ',
         COL_RED),
        (8.2, 1.3, 3.5, 1.5, 'T6: Lattice Anisotropy Decay',
         'epsilon_4(R) = O((Delta x/R)^2)\nContinuum limit conditional',
         COL_RED),
    ]

    for x, y, w, h, name, content, color in theorems:
        rect = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.05',
                              edgecolor=color, facecolor=color + '18',
                              linewidth=1.8)
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h - 0.25, name, ha='center', va='top',
                fontsize=9.5, fontweight='bold', color=color)
        ax.text(x + w / 2, y + h - 0.7, content, ha='center', va='top',
                fontsize=8, color=COL_PRIMARY, family='monospace')

    # Arrows from axioms to theorems
    for tx in [2.05, 6.0, 9.95]:
        arrow = FancyArrowPatch((tx, 5.5), (tx, 5.0),
                                arrowstyle='->', color=COL_GREY,
                                mutation_scale=12, linewidth=1.5)
        ax.add_patch(arrow)
    # Spread to all 6
    for tx in [2.05, 6.0, 9.95]:
        arrow = FancyArrowPatch((tx, 5.5), (tx, 5.0),
                                arrowstyle='->', color=COL_GREY,
                                mutation_scale=12, linewidth=1.5)
        ax.add_patch(arrow)
    for tx in [2.05, 6.0, 9.95]:
        arrow = FancyArrowPatch((6, 5.5), (tx, 5.0),
                                arrowstyle='->', color=COL_GREY,
                                mutation_scale=12, linewidth=1.0,
                                alpha=0.4,
                                connectionstyle='arc3,rad=0.1')
        ax.add_patch(arrow)

    # Cross-dependencies (T1 -> T3, T4 -> T5, T5 -> T6, T1 -> T2)
    cross_deps = [
        (3.8, 4.25, 4.25, 4.25, '->'),  # T1 -> T2
        (3.8, 4.0, 4.25, 2.4, '->'),    # T1 -> T4 (no, T4 is below)
        (7.75, 4.25, 8.2, 4.25, '->'),  # T2 -> T3
        (7.75, 2.0, 8.2, 2.0, '->'),    # T4 -> T5
        (11.75, 2.0, 11.75, 3.5, '->'), # T5 -> T6
    ]
    for sx, sy, ex, ey, style in cross_deps:
        arrow = FancyArrowPatch((sx, sy), (ex, ey),
                                arrowstyle=style, color=COL_ACCENT,
                                mutation_scale=12, linewidth=1.2,
                                alpha=0.7,
                                connectionstyle='arc3,rad=0.0')
        ax.add_patch(arrow)

    # Legend at bottom
    ax.text(6, 0.7,
            'Solid grey: direct axiom derivation  ·  Solid red: inter-theorem dependency',
            ha='center', fontsize=9, color=COL_GREY, style='italic')

    return save_fig(fig, '10_theorem_graph.png')


# =============================================================================
# Main
# =============================================================================
def main():
    print("Generating FPM v5.0 Unified Framework charts...")
    chart_master_chain()
    chart_layer_architecture()
    chart_axcore_cost_surface()
    chart_viscosity_law()
    chart_galaxy_rotation()
    chart_cmb_spectrum()
    chart_closure_diagram()
    chart_calibration_bridge()
    chart_metabolic_modes()
    chart_theorem_graph()
    print(f"\nAll charts saved to {OUTPUT_DIR}/")


if __name__ == '__main__':
    main()
