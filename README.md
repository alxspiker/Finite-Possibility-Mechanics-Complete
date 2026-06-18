# FPM v5.2 — The Complete Unified Paper

**Author:** Alx Spiker · AperioGenix · Edmonton, Alberta, Canada
**Date:** 18 June 2026
**Version:** v5.2 — Complete Unified Paper (single document)

## What's in this package

```
FPM_v52_Complete/
├── README_v52.md                                  # This file
├── FPM_v52_Complete_Unified.pdf                   # The 45-page single unified paper
├── FPM_v52_Complete_Unified.md                    # Markdown summary
├── generate_fpm_v52_complete.py                   # PDF generator script
├── verify_v51_derivations.py                      # Verification script (9 checks)
├── generate_unified_charts.py                     # Chart generator (10 figures)
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
Open `FPM_v52_Complete_Unified.pdf` in any PDF reader. The document is 45 pages, organized into 10 parts (33 sections), with 10 figures and 6 tables.

### Run the verification
```bash
python verify_v51_derivations.py
```
This runs all 9 derivation checks and prints a summary. All checks pass.

### Regenerate the PDF
```bash
pip install reportlab matplotlib numpy pillow
python generate_unified_charts.py    # Regenerates all 10 diagrams
python generate_fpm_v52_complete.py  # Regenerates the PDF
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
- §7 The Four Closure Theorems
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

### Part VII: Calibration & G_FPM (with full derivation inline)
- §24 Derivation of the Universal Engine Tick
- §25 Derivation of G_FPM (8-step derivation, 0.04% from CODATA)
- §26 Derivation of the AxCore-to-FPM Calibration Factor = 80

### Part VIII: Numerical Validation
- §27 Ten experiments summary

### Part IX: Master Chain & Open Frontiers
- §28 The Master Chain Equation
- §29 Open Frontiers
- §30 Final Verdict

### Part X: Appendices
- §31 Complete Derivation Tree (21 derived quantities)
- §32 Symbol Reference
- §33 Verification Summary

## The 21 Derived Quantities (zero fitted constants)

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
| G_FPM (gravity) | 6.677×10⁻¹¹ | §25 |
| calib (AxCore factor) | 80 | §26 |
| Δt_univ (universal tick) | 1.152×10⁻²³ s | §24 |
| Δx_univ (lattice constant) | 3.453 fm | §24 |

## Verification Results

All 9 derivation checks pass:

| # | Derivation | Computed | Target | Match |
|---|------------|----------|--------|-------|
| 1 | 9:1 channel split (α, β) | 0.2, 1.8 | 0.2, 1.8 | exact |
| 2 | Viscosity bounds [0.50, 0.85] | 0.50, 0.85 | 0.50, 0.85 | exact |
| 3 | 3/4 exponent | −3/4 | −3/4 | exact |
| 4 | 16/3 ledger inertia | 5.333 | 5.333 | exact |
| 5 | Lag ceiling γ_max | 31.8739 | 31.8739 | exact |
| 6 | Point-Pair α_PP | 702.628349 | 702.628349 | 6.4e-13 rel. |
| 7 | CMB A_FPM, n_s, r, ℓ_D | 4.04e-5, 0.969, 0.0035, 1310 | — | all in range |
| 8 | G_FPM | 6.677e-11 | 6.674e-11 (CODATA) | 0.04% off |
| 9 | Calibration factor | 80 | 80 | exact |

## The Five Axioms (the only inputs)

| Axiom | Statement |
|-------|-----------|
| A1 | Finite substrate (ℤ³, finite memory, finite energy) |
| A2 | Thermodynamic route cost (AxCore operational instantiation) |
| A3 | Closed universe (internal redistribution only) |
| A4 | Discrete causal ticks (irreversible order) |
| A5 | Calibration (max propagation = c) |

**No further postulates appear anywhere in the paper.**

## What's different from v5.0/v5.1

- **v5.0** was the interpretive framework (what things mean) — 41 pages
- **v5.1** was the pure derivation document (how things are proven) — 28 pages
- **v5.2** (this) is the **single unified paper** that combines both, with all derivations inline where they belong — 45 pages

The v5.2 paper is the definitive document. It contains everything from v5.0 and v5.1 in a single coherent narrative.

## The Deepest Result

The FPM v5.2 framework is a fully axiomatic system. Every observable prediction is a theorem of the five axioms. The framework's empirical engagements (SPARC, Planck, CODATA) are genuine tests of the axioms, not fits to data.

**The 0.04% match to CODATA G, the 0.45% match to Planck dark-to-baryonic ratio, and the 0.54% match to Planck TT RMS are all derived predictions, not fitted parameters.**

---

*FPM v5.2 · Complete Unified Paper · 18 June 2026*
