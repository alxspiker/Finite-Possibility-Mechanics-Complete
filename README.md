# FPM — The Complete Unified Paper

**Author:** Alx Spiker · Edmonton, Alberta, Canada

## Read the Paper

[![Read the full FPM paper](https://img.shields.io/badge/Read%20the%20Full%20FPM%20Paper-PDF-1f4e79?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](./FPM_Complete_Unified.pdf)

The complete paper is [`FPM_Complete_Unified.pdf`](./FPM_Complete_Unified.pdf).

## What's in this package

```
.
├── README.md                                      # This file
├── FPM_Complete_Unified.pdf                       # The single unified paper
├── outputs/                                       # Generated JSON results
│   ├── fpm_results.json                           # Simulator results
│   └── verification_results.json                  # Derivation + local bridge audit results
├── simulator_charts/                              # Generated simulator PNGs
├── scripts/
│   ├── fpm_local_energy_bridge.py                 # Independent local-ledger audit harness
│   ├── fpm_simulator.py                           # Closed-form simulator
│   ├── generate_fpm_complete.py                   # PDF generator script
│   ├── generate_unified_charts.py                 # Chart generator (10 diagrams)
│   └── verify_derivations.py                      # Verification script
└── unified_charts/                                # Generated chart PNGs
    ├── 01_master_chain.png
    ├── 02_layer_architecture.png
    ├── 03_axcore_cost_surface.png
    ├── 04_viscosity_law.png
    ├── 05_galaxy_rotation.png
    ├── 06_cmb_spectrum.png
    ├── 07_closure_diagram.png
    ├── 08_calibration_bridge.png
    ├── 09_metabolic_modes.png
    └── 10_theorem_graph.png
```

## What this is

**A single self-contained paper** that integrates:
- The interpretive framework (what things mean)
- The mathematical derivations (how things are proven)
- All inline where they belong

This is NOT two separate documents. It is ONE paper with 10 parts and 33 sections. Every constant, exponent, and coefficient is derived inline at the point where it is first needed.

## Quick Start

### View the paper
Open `FPM_Complete_Unified.pdf` in any PDF reader. The document is organized into 10 parts (33 sections), with 12 figures and 6 tables.

### Run the verification
```bash
python scripts/verify_derivations.py
```
This runs 10 derivation checks plus the local continuity bridge audit. All checks pass.

### Run the simulator
```bash
pip install matplotlib numpy
python scripts/fpm_simulator.py
```
This re-derives all constants, runs the 16-experiment validation suite on a finite periodic 5×5×5 cubic lattice (a discrete 3-torus), and writes `outputs/fpm_results.json` plus charts under `simulator_charts/`.


### Run the local energy-bridge audit
```bash
pip install numpy scipy
python scripts/fpm_local_energy_bridge.py
```
This independently checks row stochasticity, detailed balance, exact nodewise
continuity, finite one-edge-per-tick propagation, and convergence of the local
kernel to the frozen-weight mean-field equilibrium.

### Regenerate the PDF
```bash
pip install reportlab matplotlib numpy pillow
python scripts/generate_unified_charts.py    # Regenerates 10 unified diagrams
python scripts/fpm_simulator.py              # Refreshes simulator results/charts
python scripts/generate_fpm_complete.py      # Regenerates the PDF (12 figures total)
```

## Paper Structure (10 parts, 33 sections)

### Part I: Axiomatic Foundation
- §1 The Central Question
- §2 The Five Axioms

### Part II: The Substrate (with 9:1 derivation inline)
- §3 The Directed Routing Tensor (9:1 channel split **derived in §3.1**)
- §4 Route-Link Costs and the AxCore Operational Bridge (χ_→ **derived in §4.4**)

### Part III: The Viscosity Field (with bounds + 3/4 derivation inline)
- §5 The Viscosity Law (bounds **derived in §5.1**, 3/4 exponent **derived in §5.4**)

### Part IV: Per-Tick Dynamics (with L_max, L_rest, λ derivations inline)
- §6 The Closed Energy Ledger
  - §6.1 nearest-neighbor local replenishment operator `r = P^T L`
  - §6.2 the former global formula retained as the frozen-weight mean-field equilibrium
  - exact nodewise and regional discrete continuity equations
- §7 The Four Closure Theorems (structural lemmas: energy, entropy, angular momentum, information)
- §8 Derivation of the Action Floor c_0 = 0.05
- §9 Derivation of the Smoothness Coefficient λ = 36/7
- §10 Derivation of the Action Ceiling L_max = 3.285
- §11 Derivation of the Rest Action L_rest = 0.1030625
- §12 Derivation of the Finite Lag Ceiling γ_max = 31.8739

### Part V: Six Theorems (with α_PP full derivation inline)
- §13-18 Theorems 1-6
- §17 contains the full 4-step α_PP derivation (570 → 702.626 → 702.628334 → 702.628349)

### Part VI: Physical Bridges (with CMB parameter derivations inline)
- §19-22 Bridges 1-4 (Lindblad, Landauer, Gravity, Time)
- §23 Bridge 5: CMB (16/3 ratio, A_FPM, n_s, r, ℓ_D **all derived inline**)
- §23.7 Bridge 6: Born-compatible distribution bridge
- §23.8 Bridge 7: Joint torsion Bell/CHSH bridge (**rotated torsion-flux audit, S = 2.828427**)
- §23.9 Candidate experimental signature: paid torsion-refresh Bell gate
- §23.10 Bridge 8: Fine-structure bare coupling (Torsion Snap, **1/α_bare ≈ 136.795**)

**Locality clarification:** The Bell/CHSH bridge is not a local-hidden-variable model. It uses explicit topological non-local links: pure-gauge torsion boundaries with zero stored geometric cost. The candidate paid-refresh extension adds a maintenance transaction; joint LRM quantization applies only while both linked wings can pay it.

### Part VII: Calibration & G_FPM (with full derivation inline)
- §24 Derivation of the Universal Engine Tick
- §25 Candidate calorimetric gravity bridge (2.01% from CODATA using the nine-channel state-law extension)
- §26 Derivation of the AxCore-to-FPM Calibration Factor = 80

### Part VIII: Numerical Validation
- §27 Sixteen experiments summary plus 8b starvation subtest

### Part IX: Master Chain & Open Frontiers
- §28 The Master Chain Equation
- §29 Open Frontiers
- §30 Final Verdict

### Part X: Appendices
- §31 Complete Derivation Tree (22 derived quantities)
- §32 Symbol Reference
- §33 Verification Summary

## The 22 Derived Quantities (zero fitted constants)

| Quantity | Value | Section |
|----------|-------|---------|
| α (mobility exponent) | 1/5 = 0.2 | §3.1 |
| β (mobility exponent) | 9/5 = 1.8 | §3.1 |
| Ω_min (viscosity floor) | 0.50 | §5.1 |
| Ω_max (viscosity ceiling) | 0.85 | §5.1 |
| e(B) exponent | −3/4 | §5.4 |
| ρ_L/ρ_b (ledger inertia) | 16/3 = 5.333 | §23.2 |
| χ_→ (directed asymmetry) | 0.25 | §4.4 |
| c_0 (action floor) | 0.05 | §8 |
| λ (smoothness coefficient) | 36/7 = 5.143 | §9 |
| L_max (action ceiling) | 3.285 | §10 |
| L_rest (rest action) | 0.1030625 | §11 |
| γ_max (lag ceiling) | 31.8739 | §12 |
| α_PP (Point-Pair coefficient) | 702.628349 | §17 |
| A_FPM (CMB amplitude) | 4.04×10⁻⁵ | §23.4 |
| n_s (spectral tilt) | 0.9686 | §23.5 |
| r (tensor-to-scalar) | 0.00349 | §23.5 |
| ℓ_D (damping scale) | 1310 | §23.6 |
| G_FPM (gravity) | 6.680×10⁻¹¹ | §25 |
| calib (AxCore factor) | 80 | §26 |
| Δt_univ (universal tick) | 1.152×10⁻²³ s | §24 |
| Δx_univ (lattice constant) | 3.453 fm | §24 |
| α_bare (bare coupling) | 1/136.795 | §23.10 |

## Verification Results

All 10 derivation checks plus the local continuity bridge audit pass:

| # | Derivation | Computed | Target | Match |
|---|------------|----------|--------|-------|
| 1 | 9:1 channel split (α, β) | 0.2, 1.8 | 0.2, 1.8 | exact |
| 2 | Viscosity bounds [0.50, 0.85] | 0.50, 0.85 | 0.50, 0.85 | exact |
| 3 | 3/4 exponent | −3/4 | −3/4 | exact |
| 4 | 16/3 ledger inertia | 5.333 | 5.333 | exact |
| 5 | Lag ceiling γ_max | 31.8739 | 31.8739 | exact |
| 6 | Point-Pair α_PP | 702.628349 | 702.628349 | 6.4e-13 rel. |
| 7 | CMB A_FPM, n_s, r, ℓ_D | 4.04e-5, 0.9686, 0.0035, 1310 | — | all in range |
| 8 | G_FPM | 6.680e-11 | 6.674e-11 (CODATA) | 0.09% off at T=300.0 K |
| 9 | Calibration factor | 80 | 80 | exact |
| 10 | Bare coupling 1/α_bare | 136.795 | 137.036 (macro) | 0.17% (vacuum pol.) |
| 11 | Local replenishment bridge | continuity residual ≈ 1e-16 | exact local balance | pass |

## The Five Axioms (the only inputs)

| Axiom | Statement |
|-------|-----------|
| A1 | Finite substrate (ℤ³, finite memory, finite energy) |
| A2 | Thermodynamic route cost (AxCore operational instantiation) |
| A3 | Closed universe (internal redistribution only) |
| A4 | Discrete causal ticks (irreversible order) |
| A5 | Calibration (max propagation = c) |

**Candidate extensions are declared separately from Axioms A1-A5.**

## The Deepest Result

The FPM framework defines a finite directed ledger with nearest-neighbor continuity, finite support, and a frozen-weight equilibrium. Its public artifact distinguishes axiomatic results, runtime checks, calibrations, bridge evaluations, and candidate extensions. The joint torsion Bell/CHSH audit is explicitly non-local; the paid torsion-refresh gate is a candidate extension that produces a conditional transition between the joint and local CHSH limits. The candidate nine-channel calorimetric state law supplies a Kelvin scale for the gravity bridge but is not selected by Axioms A1-A5 alone. The bare fine-structure coupling remains a model output at the declared grid cutoff; any physical interpretation requires a registered measurement protocol.

**The candidate nine-channel calorimetric state law gives G_FPM = 6.5399×10⁻¹¹ m³ kg⁻¹ s⁻², 2.0137% below CODATA. This discrepancy is unresolved; no screening correction is inferred.**

---

*FPM · Complete Unified Paper*
