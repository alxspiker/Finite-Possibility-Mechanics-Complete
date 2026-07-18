#!/usr/bin/env python3
"""Generate Modular Paper 02: Executable FPM."""

from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Spacer

from _paper_template import PaperSpec, body, build_manuscript, bullet, equation, h1, h2, reference, statement


SPEC = PaperSpec(
    number=2,
    title="Executable FPM",
    subtitle="Reference Runtime, Numerical Contract, and Reproducible Audit",
    filename="02_Executable_FPM.pdf",
    scope="The executable specification and numerical audit of the public FPM reference simulator.",
    claim_boundary="The runtime implements Paper 1's local transport and signed-ledger mechanics. The exact-cochain torsion construction is a separate bridge obligation deferred to Paper 5.",
    sections=[
        ("Abstract", "Implementation result."),
        ("Executable specification", "The role of the reference runtime."),
        ("Geometry and state", "Periodic cubic lattice and per-node state."),
        ("Update pipeline", "Ordered master-chain execution."),
        ("Numerical realization", "Floating-point semantics and tolerances."),
        ("Conservation audit", "Local and expanded-ledger checks."),
        ("Validation suite", "Sixteen primary experiments and starvation subtest."),
        ("Reproduction protocol", "Commands, outputs, and determinism."),
        ("Regression classification", "Invariant and geometry-dependent results."),
        ("Conclusion", "Executable result."),
        ("References", "Source and numerical foundations."),
    ],
    document_label="COMPUTATIONAL PAPER",
)


def manuscript(styles):
    s=[]
    s += [
        h1("Abstract", styles),
        body("This paper specifies the public Python reference implementation of Finite Possibility Mechanics. The runtime executes the FPM master chain on a periodic 5&times;5&times;5 cubic lattice: 125 nodes, six nearest neighbours per node, and 400 ordered ticks in the standard production audit. Each node carries stored energy, a directed 3&times;3 route ledger, a nine-channel complex carrier, viscosity, prior, cache bias, and derived observables. Ordinary action is replenished through the local reversible kernel proved in Paper 1; capacity overflow, starvation, Landauer debit, and explicit torsion-link operations are recorded in separate signed accounts.", styles),
        body("The implementation reproduces the exact algebraic identities to floating-point precision. The local bridge audit reports row-stochastic error 1.11&times;10<sup>-16</sup>, detailed-balance error 2.78&times;10<sup>-17</sup>, nodewise continuity residual 6.94&times;10<sup>-17</sup>, exact local energy edge-flux antisymmetry, and equilibrium L1 error 7.28&times;10<sup>-14</sup>. The 400-tick master run closes the expanded ledger to 6.40&times;10<sup>-14</sup> while exercising capacity routing, starvation, information erasure, finite microcell quantization, and linked torsion quantization. These results establish a reproducible executable specification whose numerical residuals are many orders below the modeled action scales.", styles),
        statement("Computational result", "The public runtime implements the finite periodic cubic geometry and local replenishment theorem directly. Its residuals are implementation checks of the stated equations; they are not unrecorded energy channels or independent physical evidence.", styles),
        Spacer(1, 4 * mm),
        body("<b>Record DOI:</b> <a href='https://doi.org/10.5281/zenodo.21420643'>https://doi.org/10.5281/zenodo.21420643</a>", styles),
    ]
    s += [
        h1("1. Executable specification", styles),
        body("A mathematical model becomes operational only when every state variable, update order, boundary branch, and observable has an executable meaning. The reference simulator serves that role for FPM. It is deliberately transparent: all constants are constructed in one derivation object, all experiments return machine-readable records, every chart is generated from those records, and output paths are explicit.", styles),
        h2("1.1 Scope of the reference runtime", styles),
        bullet("Instantiate the finite graph, directed ledger, carrier, viscosity, action, and signed energy accounts.", styles),
        bullet("Evaluate the master chain tick by tick with a fixed seed.", styles),
        bullet("Run theorem checks and physical correspondence diagnostics as separate named experiments.", styles),
        bullet("Write JSON results to <font face='Courier'>outputs/</font> and charts to <font face='Courier'>simulator_charts/</font> by default.", styles),
        bullet("Provide a readable real-valued reference against which an exact integer engine can be compared.", styles),
        h2("1.2 Source boundary", styles),
        body("The executable specification is contained in <font face='Courier'>scripts/fpm_simulator.py</font>, with independent algebraic checks in <font face='Courier'>scripts/verify_derivations.py</font> and the focused local-transport harness <font face='Courier'>scripts/fpm_local_energy_bridge.py</font>. The generator and paper consume their outputs; they do not silently recompute alternative results.", styles),
        body("This executable scope includes Paper 1's stochastic kernel, detailed balance, local and regional energy continuity, finite propagation cone, activity-weighted equilibrium, and expanded signed ledger. It does not yet construct an edge 1-cochain &phi;, compute a plaquette coboundary A=d&phi;, or audit periodic cohomology sectors. Consequently, antisymmetric internal route matrices and explicit torsion links are bridge ansatzes here, not an executable proof of Paper 1's conditional exact-cochain theorem. Paper 5 must supply and test that map.", styles),
    ]
    s += [
        h1("2. Geometry and state", styles),
        h2("2.1 Periodic cubic lattice", styles),
        equation("&Lambda;<sub>5</sub> = (Z/5Z)<sup>3</sup>, &nbsp;&nbsp; |&Lambda;<sub>5</sub>|=125, &nbsp;&nbsp; deg(i)=6", styles),
        body("Coordinates are enumerated modulo five. The neighbour map adds and subtracts one unit on each axis with periodic wraparound. Side length five is large enough that the positive and negative neighbour on every axis is distinct. The same six-neighbour map is supplied to ordinary replenishment and local overflow routing, so the geometry does not change between the interior and capacity branches.", styles),
        h2("2.2 Per-node state", styles),
        equation("X<sub>i,t</sub>=(E,R,&psi;,b,&tau;,&pi;,&Omega;<sub>prev</sub>)<sub>i,t</sub>", styles),
        body("E is stored energy; R is the 3&times;3 directed route ledger; &psi; in C<sup>9</sup> is the normalized carrier; b is cache bias; &tau; is the local truth target; &pi; is the fallback prior; and &Omega;<sub>prev</sub> stores the preceding viscosity for the smoothness cost. The symbols &tau; and &pi; are lowercase and match Paper 1 and the runtime fields <font face='Courier'>tau</font> and <font face='Courier'>pi</font>; &pi; is not the equilibrium vector &rho;<super>eq</super>. The current viscosity &Omega;, the binary projections p<sub>L</sub> and p<sub>R</sub>, and coherence c are derived from this stored state rather than evolved as independent variables.", styles),
        body("Paper 2 names these carrier fields because the unified runtime must allocate and update them in one transaction. Their normalization constraints, phase dynamics, low-energy consolidation, finite microcell rule, and Landauer accounting are derived in Paper 3. Until that dependency is established, the present paper treats those routines as declared downstream modules and audits only their executable interfaces and ledger effects.", styles),
        h2("2.3 Standard initial condition", styles),
        body("The production run uses pseudorandom seed 17 and initializes 125 nodes near the balanced carrier state. Each node starts with 0.5 normalized energy units. Because the derived ceiling is E<sub>max</sub>=2/3, this is 75% of capacity and gives total initial stored energy 62.5. The run begins near the normal operating viscosity, and all perturbations are small and reproducible. Torsion links are created as explicit node pairs rather than inferred from distance.", styles),
    ]
    s += [
        h1("3. Ordered update pipeline", styles),
        body("One tick is an ordered transaction. Later operations consume the state written by earlier operations, implementing Axiom A4 directly.", styles),
        h2("3.1 Tick sequence", styles),
        bullet("Compute route-ledger invariants, normalized entropy and balance, spectral weights, capacity, and viscosity.", styles),
        bullet("Evaluate the declared semantic and geometric action terms plus the viscosity-smoothness term.", styles),
        bullet("If action is unaffordable, pay what is available and record the remainder as starvation deficit.", styles),
        bullet("Construct activity weights and the six-neighbour local kernel; apply r=P<super>T</super>L.", styles),
        bullet("Route positive capacity overflow to adjacent available capacity; record unabsorbed remainder as exhaust.", styles),
        bullet("Rotate each carrier channel by its route-cost phase and refresh scalar projections.", styles),
        bullet("Apply low-energy consolidation, finite microcell selection, and Landauer debit when the gate is active.", styles),
        bullet("Apply explicitly linked joint-torsion operations through their separate branch.", styles),
        bullet("Commit state and append stored-energy, expanded-ledger, action, viscosity, dispersion, and event diagnostics.", styles),
        h2("3.2 Interior replenishment", styles),
        equation("r<sub>t</sub>=P<sub>t</sub><super>T</super>L<sub>t</sub>, &nbsp;&nbsp; E<sub>raw,t+1</sub>=E<sub>t</sub>-L<sub>t</sub>+r<sub>t</sub>", styles),
        body("The simulator constructs P from the exact formula in Paper 1 and validates the matrix before use. The transpose is intentional: rows describe where each source sends its paid action, while P<super>T</super>L collects what each destination receives.", styles),
        h2("3.3 Capacity resolver", styles),
        body("For E<sub>raw</sub>&gt;E<sub>max</sub>, the excess is offered only to the same six neighbouring sites, weighted by their available capacity. Concurrent proposals are accumulated and limited by receiving capacity. Any unaccepted remainder enters thermal exhaust. For E<sub>raw</sub>&lt;0, the state is clipped to zero and the unpaid amount enters starvation deficit. These events alter stored energy but close the expanded ledger exactly in real arithmetic.", styles),
        body("In the notation of Paper 1, exhaust and paid erasure increment the local positive event ledger X<sub>i</sub>, while an unpaid zero-boundary amount increments the local deficit ledger D<sub>i</sub>. The runtime retains the site-resolved increments for each tick and then forms the observer totals X(t)=&Sigma;<sub>i</sub>X<sub>i</sub>(t) and D(t)=&Sigma;<sub>i</sub>D<sub>i</sub>(t) used by Theorem 8. Summation occurs after the local event; it is an audit reduction, not a propagating signal.", styles),
    ]
    s += [
        h1("4. Numerical realization", styles),
        h2("4.1 Why the reference uses floating point", styles),
        body("The Python implementation uses IEEE-754 double precision [5] and NumPy complex arrays because it is the clearest representation of the equations. It preserves direct correspondence between source expressions and the manuscript, supports singular-value decomposition and phase rotation naturally, and makes sensitivity analysis inexpensive. This is a reference semantics, not a claim that physical state is binary floating-point data.", styles),
        body("Tensorless is not assumed to be this runtime with floating point replaced by integers. Its synchronous sandbox receives caller-translated action and payload values, resolves contention with exact integer policies, and currently replenishes through a global proportional allocator. That allocator realizes an equilibrium-style activity weighting, not the ordinary one-tick local kernel r=P<super>T</super>L used here. Tensorless also reports aggregate exhaust and starvation counters rather than this runtime's site-resolved event history. Paper 4 specifies those differences and limits cross-runtime comparisons to explicitly shared contracts.", styles),
        h2("4.2 Residual interpretation", styles),
        body("An algebraic identity that is exact over real numbers may leave a residual near 10<sup>-16</sup> after a sequence of floating-point additions and multiplications. The correct test is scale-aware: compare the residual with machine precision and the magnitude of the summed quantities, then verify convergence or exact agreement in an integer realization. The reference audit records residuals instead of rounding them to zero in the output.", styles),
        statement("Numerical contract", "Every reported residual is an observable of the implementation. PASS means the stated criterion was met; it does not rewrite the measured residual as mathematical zero.", styles),
        h2("4.3 Reproducibility controls", styles),
        bullet("Fixed random seeds for stochastic initialization and theorem trials.", styles),
        bullet("Deterministic lattice enumeration and neighbour ordering.", styles),
        bullet("Named output directories, overridable through environment variables.", styles),
        bullet("JSON serialization of axioms, derived values, theorem records, bridge records, experiments, and the master trajectory.", styles),
        bullet("Charts regenerated from the same in-memory result object written to JSON.", styles),
    ]
    s += [
        h1("5. Conservation audit", styles),
        h2("5.1 Focused local bridge", styles),
        body("The independent local-energy harness checks the kernel on non-uniform positive weights and viscosities. Its current results are:", styles),
        bullet("row-stochastic residual: 1.11&times;10<sup>-16</sup>", styles),
        bullet("stationary-weight residual: 6.94&times;10<sup>-18</sup>", styles),
        bullet("detailed-balance residual: 2.78&times;10<sup>-17</sup>", styles),
        bullet("global replenishment residual: 3.55&times;10<sup>-15</sup>", styles),
        bullet("nodewise continuity residual: 6.94&times;10<sup>-17</sup>", styles),
        bullet("local energy edge-flux antisymmetry residual: exactly 0 in the evaluated representation", styles),
        bullet("support radii after ticks 0 through 8: 0,1,2,3,4,5,6,7,8", styles),
        bullet("equilibrium L1 residual: 7.28&times;10<sup>-14</sup>", styles),
        h2("5.2 Master-chain ledger", styles),
        body("The 400-tick production trajectory begins with total stored energy 62.5. Once boundary and special branches activate, stored energy changes; this is expected. The expanded ledger remains 62.5 to a maximum residual of 6.40&times;10<sup>-14</sup>. The run records 67.6694 units of locally routed spillover, 16.1690 units of external thermal exhaust, 23.2968 units of starvation deficit, and 1.7619&times;10<sup>-7</sup> units of Landauer debit. It also executes 3,842 finite microcell quantizations and 1,921 linked torsion quantizations.", styles),
        statement("Ledger reading", "The simulator does not conserve stored node energy at every tick. It conserves ordinary interior replenishment locally and the expanded signed ledger across all declared branches.", styles),
    ]
    s += [
        h1("6. Validation suite", styles),
        body("The suite contains sixteen primary experiments plus one starvation subtest. Their roles differ: some test mathematical invariants, some test numerical implementation, and some evaluate physical bridge formulae. The domain-specific names below are regression labels for downstream correspondences developed in Papers 5 and 6; understanding how a route ledger is mapped to dephasing, galaxy data, or a Bell test is not a prerequisite for auditing the runtime contract in this paper. Paper 6 supplies the full evidence hierarchy. The current runtime records the following headline results.", styles),
        bullet("Dispersion contraction: 0 violations in 6,000 evaluated updates.", styles),
        bullet("Lindblad correspondence: algebraic implementation check, RMSE 1.79&times;10<sup>-102</sup> for the selected zero-target dephasing map.", styles),
        bullet("Closed-universe conservation: final floating-point drift 7.96&times;10<sup>-14</sup> percent.", styles),
        bullet("Spectral-gap weights: isotropic leading weight 1/3.", styles),
        bullet("Mean-field truth closure: final mismatch 0.02637 in the declared convergence experiment.", styles),
        bullet("Point-Pair iteration: self-consistency check; the declared fixed-point equation closes with zero residual in evaluated binary64 arithmetic.", styles),
        bullet("Bounded depletion: effective floor 0.0314 at load 10<sup>6</sup>.", styles),
        bullet("Semantic-entropy ledger: saturated closure in the specified erasure transaction.", styles),
        bullet("Wrong-lock starvation subtest: starvation begins at tick 1.", styles),
        bullet("Finite lag construction: ratio 31.8738629472.", styles),
        bullet("SPARC gas-boundary bridge: archived, unregenerated benchmark metadata reports median RMSE 11.61 km/s. With external tables absent, the public runtime reports the empirical audit unavailable and does not emit a competitive verdict.", styles),
        bullet("Exact carrier capacity: 1,452,997,909 bit-equivalent slots.", styles),
        bullet("Born finite allocation: maximum total-variation error 1.20&times;10<sup>-9</sup>.", styles),
        bullet("Joint torsion CHSH: S=2.8284271261 in the implemented joint rule.", styles),
        bullet("Runtime linked quantization: the linked pair enters one joint ledger operation.", styles),
        bullet("Bare coupling construction: inverse coupling 136.7946397586.", styles),
        bullet("Local replenishment bridge: maximum continuity residual 6.94&times;10<sup>-17</sup>.", styles),
    ]
    s += [
        h1("7. Reproduction protocol", styles),
        h2("7.1 Standard commands", styles),
        equation("python3 scripts/verify_derivations.py", styles),
        equation("python3 scripts/fpm_local_energy_bridge.py", styles),
        equation("python3 scripts/fpm_simulator.py", styles),
        body("The simulator creates the output directory if required. <font face='Courier'>FPM_OUTPUT_DIR</font> redirects JSON files and <font face='Courier'>FPM_SIMULATOR_CHARTS_DIR</font> redirects charts without changing the equations. A valid reproduction retains the emitted JSON, console summary, environment, Python and dependency versions, and source commit identifier.", styles),
        h2("7.2 Expected artifacts", styles),
        bullet("<font face='Courier'>outputs/verification_results.json</font>: focused derivation and local-bridge checks.", styles),
        bullet("<font face='Courier'>outputs/fpm_results.json</font>: complete axioms, constants, theorem records, bridges, experiments, and trajectory.", styles),
        bullet("<font face='Courier'>simulator_charts/*.png</font>: plots generated from the same run.", styles),
        h2("7.3 Reproduction criterion", styles),
        body("Exact decimal equality is required for integer and rational constructions. Floating-point arrays are compared using declared absolute or relative criteria appropriate to their scale. Geometry-dependent stochastic trajectories must reproduce under the same seed and software stack; cross-platform runs should reproduce all classifications and agree within the stated numerical tolerance.", styles),
    ]
    s += [
        h1("8. Regression classification", styles),
        h2("8.1 Invariants", styles),
        body("Row sums, local energy-flux antisymmetry, signed-ledger identity, neighbour count, carrier normalization, exact integer capacity, and support-cone growth are structural invariants. A geometry change does not license these to drift. This energy-flux test is distinct from the conditional exact-cochain construction for directed asymmetry in Paper 1.", styles),
        h2("8.2 Geometry-dependent observables", styles),
        body("Mixing time, transient stored-energy curves, event counts, mean viscosity, mean action, and spatial correlation patterns depend on lattice size and adjacency. The upgrade from a one-dimensional ring to the 125-node cubic lattice legitimately changed these outputs. Regression tests therefore compare them with geometry-matched baselines rather than forcing historical values to persist.", styles),
        h2("8.3 Bridge-dependent observables", styles),
        body("Galaxy, CMB, Bell, and coupling results depend on bridge definitions in addition to the runtime core. They are reported in the same executable package for traceability, but a change in one bridge must not be interpreted as a failure of local conservation unless the relevant foundational invariant also changes.", styles),
    ]
    s += [
        h1("9. Conclusion", styles),
        body("Executable FPM is a transparent real-valued implementation of the finite local mechanics defined in Paper 1. It runs the intended six-neighbour cubic geometry, uses the same adjacency for ordinary replenishment and local overflow, records every non-interior energy branch, and exposes both stored energy and the expanded closed ledger. The numerical results confirm the exact algebra at machine precision while preserving the measured residuals.", styles),
        body("This reference now provides the common executable target for two complementary developments: Paper 3's finite carrier and information dynamics, and Paper 4's deterministic exact-integer realization. The Python runtime prioritizes mathematical visibility; the exact engine prioritizes arithmetic closure and operational determinism. Agreement between them is the strongest implementation audit available to the framework.", styles),
        statement("Executable summary", "The public runtime is not a diagram of the theory. It is the theory's finite local update chain, executed on 125 six-neighbour nodes and audited transaction by transaction.", styles),
        PageBreak(),
        h1("References", styles),
        reference("[1] A. Spiker, <i>Finite-Possibility-Mechanics-Complete</i>, source repository and reproducible runtime. <a href='https://github.com/alxspiker/Finite-Possibility-Mechanics-Complete'>https://github.com/alxspiker/Finite-Possibility-Mechanics-Complete</a>", styles),
        reference("[2] A. Spiker, <i>FPM Foundations: Finite Local Substrates, Directed Route Ledgers, and Exact Closure</i>, Modular Paper 01, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21420508'>https://doi.org/10.5281/zenodo.21420508</a>", styles),
        reference("[3] A. Spiker, <i>Finite Possibility Mechanics: A Unified Information-Theoretic Framework</i>, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21352386'>https://doi.org/10.5281/zenodo.21352386</a>", styles),
        reference("[4] A. Spiker, <i>FPM Reference Python Simulator and Audit Results</i>, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21420735'>https://doi.org/10.5281/zenodo.21420735</a>", styles),
        reference("[5] IEEE Computer Society, <i>IEEE Standard for Floating-Point Arithmetic</i>, IEEE 754-2019. <a href='https://doi.org/10.1109/IEEESTD.2019.8766229'>https://doi.org/10.1109/IEEESTD.2019.8766229</a>", styles),
        reference("[6] N. Metropolis et al., “Equation of State Calculations by Fast Computing Machines,” <i>Journal of Chemical Physics</i> 21, 1087–1092 (1953). <a href='https://doi.org/10.1063/1.1699114'>https://doi.org/10.1063/1.1699114</a>", styles),
    ]
    return s


if __name__ == "__main__":
    print(build_manuscript(SPEC, manuscript))
