#!/usr/bin/env python3
"""Generate Modular Paper 05: Phenomenological Bridges."""

from reportlab.platypus import PageBreak

from _paper_template import (
    PaperSpec, body, build_manuscript, bullet, equation, h1, h2, reference,
    statement,
)


SPEC = PaperSpec(
    number=5,
    title="Phenomenological Bridges",
    subtitle="Route-Cost Correspondences with Quantum, Gravitational, and Cosmological Observables",
    filename="05_Phenomenological_Bridges.pdf",
    scope="Physical bridge maps from the common FPM route-cost dynamics.",
    claim_boundary="Each bridge is classified by what is derived, selected, calibrated, and tested.",
    sections=[],
    document_label="BRIDGE PAPER",
)


def manuscript(st):
    s = [
        h1("Abstract", st),
        body("Finite Possibility Mechanics supplies one microscopic accounting structure: a bounded directed route ledger, a constitutive viscosity field, a finite action budget, and local signed conservation. This paper develops the physical bridge layer that maps those internal quantities to established observables. The bridges cover pure dephasing, Landauer erasure, gravitational response, time dilation, cosmic acoustic structure, finite Born weights, Bell/CHSH correlations, and a bare electromagnetic coupling. The central result is architectural: the same route-cost variables enter every bridge, so the framework gains unification and accepts shared empirical risk.", st),
        body("The paper distinguishes four operations that are often conflated. An identity follows algebraically after definitions are fixed. A correspondence reproduces the form of an established equation. A calibration fixes dimensional scale from measured input. A prediction evaluates a pre-specified map on data not used to choose it. This classification strengthens the bridge programme by making every numerical agreement auditable without weakening the mathematical claims that are exact.", st),
        statement("Bridge result", "FPM defines a coherent family of physical hypotheses rather than unrelated curve fits. Its strongest present results are exact correspondence identities and fixed-form numerical audits; its decisive next tests are tensor galaxy morphology, a complete cosmological likelihood, resource-dependent Bell correlations, and the observable meaning of the finite lag ceiling.", st),
        body("<b>Record DOI:</b> <a href='https://doi.org/10.5281/zenodo.21420652'>https://doi.org/10.5281/zenodo.21420652</a>", st),

        h1("1. Bridge methodology", st),
        h2("1.1 Dependency stack", st),
        body("A physical bridge begins only after the foundational and executable layers are fixed. Paper 1 defines the local ledger and its conservation theorems. Paper 2 defines the real-valued reference runtime. Paper 3 defines the finite carrier, quantization, and information dynamics. Paper 4 defines an exact integer realization. The present paper asks which observable equations can be built from that shared machinery.", st),
        equation("axioms &rarr; route ledger R &rarr; viscosity &Omega; &rarr; action L &rarr; carrier &Psi; &rarr; observable bridge", st),
        h2("1.2 Evidence labels", st),
        bullet("<b>Derived:</b> follows from stated definitions and earlier results without fitting an additional coefficient.", st),
        bullet("<b>Constitutive:</b> a declared physical rule selecting one model from a wider admissible family.", st),
        bullet("<b>Calibrated:</b> uses an observed dimensional scale or reference constant.", st),
        bullet("<b>Audited:</b> evaluated numerically against an established equation or dataset.", st),
        bullet("<b>Predictive:</b> fixed before application to data capable of rejecting it.", st),
        body("A bridge can occupy more than one category. For example, the dephasing recurrence is derived from the selected carrier update and then audited against a Lindblad channel. The gravitational constant calculation is algebraically determined after a temperature and scale map are selected, but its dimensional normalization is calibrated.", st),
        h2("1.3 Dimensional discipline", st),
        body("Internal FPM variables are normalized. A bridge to SI observables therefore requires an explicit dimensional dictionary. Every such dictionary must identify its input units, calibration data, domain, and transformation law. Numerical proximity without that dictionary is not a bridge; a bridge is a reproducible map whose assumptions travel with its output.", st),

        h1("2. Lindblad correspondence", st),
        body("For the two-state projection developed in Paper 3, the selected diagnostic leaves diagonal probabilities unchanged and multiplies the off-diagonal coherence by a persistence factor kappa. With the ordinary Hamiltonian-driven part held aside, the audited update is", st),
        equation("&rho;<sub>01,t+1</sub>=&kappa;&rho;<sub>01,t</sub>, &nbsp;&nbsp; &rho;<sub>00,t+1</sub>=&rho;<sub>00,t</sub>, &nbsp;&nbsp; &rho;<sub>11,t+1</sub>=&rho;<sub>11,t</sub>, &nbsp;&nbsp; 0&le;&kappa;&le;1.", st),
        body("For kappa=exp(-Gamma Delta t), this is the finite-step pure-dephasing channel generated by the zero-Hamiltonian Lindblad form [5]. The executable audit uses the algebraically equivalent Euler parameterization gamma=(1-kappa)/Delta t. Positivity and trace preservation follow from the dephasing channel itself; no nonzero coherence target is introduced in this audit.", st),
        statement("Status", "This is an algebraic implementation correspondence for the selected zero-target pure-dephasing channel, not independent physical evidence. The physical hypothesis is that the persistence factor is controlled by FPM route burden rather than inserted as an independent environmental decay constant.", st),
        body("The runtime audit compares two implementations of that same recurrence and finds agreement down to machine precision. The discriminating experiment is not another reproduction of the selected curve; it is a test of whether measured decoherence changes with the internal route-cost variables predicted by FPM.", st),

        h1("3. Landauer bridge and mass-equivalent scale", st),
        body("Consolidation removes representable alternatives from the finite carrier. The semantic entropy decrease is converted into a thermodynamic debit through Landauer's minimum erasure cost [6]", st),
        equation("E<sub>erase</sub> &ge; k<sub>B</sub>T ln(2) per erased bit.", st),
        body("The executable ledger records that debit subject to the energy actually available. Dividing an erasure energy by c squared gives a mass-equivalent scale. Because the finite carrier contains N bit-equivalent slots, repeated erasure defines a discrete ladder rather than a continuous family:", st),
        equation("m<sub>n</sub>=n k<sub>B</sub>T ln(2)/c<sup>2</sup>, &nbsp;&nbsp; n=0,1,...,N.", st),
        body("This ladder is an energy-accounting result. A particle identification additionally requires stable dynamics, symmetry, charge, spin, lifetime, and interaction structure. The carrier capacity N=1,452,997,909 and its shell-filling radius are fixed by the finite construction in Paper 3, so the ladder spacing and endpoint are reproducible once the bridge temperature is specified.", st),
        statement("Status", "The information-to-energy inequality is established thermodynamics; applying it to FPM consolidation is a constitutive identification. The resulting mass-equivalent ladder is exact under that identification. A particle spectrum is a further dynamical problem.", st),

        h1("4. Emergent gravity and galaxy response", st),
        h2("4.1 Route-cost gradients", st),
        body("FPM proposes that matter raises local route burden, route burden changes viscosity, and spatial viscosity gradients deflect propagation. In the continuum bridge, the effective acceleration is written as a baryonic source multiplied by a dimensionless susceptibility nu_FPM. The reference audit uses", st),
        equation("&nu;<sub>FPM</sub>(x)=1+ [&Omega;<sub>max</sub>/sqrt(x+r<sub>tensor</sub>)] [1+E<sub>Z</sub>x<sup>2</sup>]<super>-&beta;</super>,", st),
        equation("g<sub>pred</sub>=&nu;<sub>gb</sub>(x)g<sub>bar</sub>, &nbsp; &nu;<sub>gb</sub>=max(10<super>-9</super>,&nu;<sub>FPM</sub>-&alpha;f<sub>gas</sub>/(1+x)).", st),
        body("Here x=|g<sub>bar</sub>|/a<sub>0</sub> is the normalized baryonic-acceleration amplitude, r<sub>tensor</sub> is the declared tensor-channel contribution, E<sub>Z</sub>=0.20E<sub>max</sub> is the consolidation threshold, and beta is inherited from the viscosity law. The gas fraction is computed at each SPARC radius from the squared velocity contributions, f<sub>gas</sub>=max(0,V<sub>gas</sub>|V<sub>gas</sub>|)/V<sub>bar</sub><sup>2</sup>, clipped to [0,1]. Thus f<sub>gas</sub> is observed source composition, not a fitted exponent; alpha=1/5 is the trace-weight coefficient from Paper 1. The low-acceleration inverse-square-root response arises from the matter-load dilution law combined with the network's minimum-connectivity shift.", st),
        h2("4.2 SPARC audit", st),
        body("An archived 99-galaxy benchmark record in the source repository [15], constructed from SPARC data [8], stores median velocity RMSE 11.61 km/s for the gas-boundary FPM source functional and 11.7156 km/s for the fixed comparison relation used by the script. The benchmark concerns the modified-dynamics class introduced by Milgrom [7], but the script's exact comparison formula is defined by its archived implementation rather than by the 1983 paper. The repository does not redistribute the SPARC tables or the archived selection and parameter ledger. Therefore these numbers are unregenerated benchmark metadata, not a current empirical result, and they receive no Level 5 evidential weight in the public artifact. When the local dataset path is absent, the runtime emits an unavailable status rather than a competitive verdict. A third-party reproduction must supply the cited data, exact selection list, parameter ledger, source revision, and regenerated outputs before making an empirical comparison claim.", st),
        statement("Empirical obligation", "The scalar rotation-curve audit must be followed by the harder tensor test: the full three-dimensional route ledger must predict non-axisymmetric morphology, lensing, and environmental dependence with one shared parameter ledger.", st),
        h2("4.3 Dimensional gravitational scale", st),
        body("The implemented dimensional map is the following explicit chain. It uses the action ceiling through L<sub>max</sub>, exact carrier capacity N, carrier radius &alpha;<sub>PP</sub> derived by the shell fixed point in Paper 3 Section 6.1, Planck constant h, electron mass m<sub>e</sub>, c, k<sub>B</sub>, and the external bath calibration T<sub>bath</sub>:", st),
        equation("&zeta;=9/(4&pi;L<sub>max</sub>), &nbsp; J=N k<sub>B</sub>T<sub>bath</sub>ln2,", st),
        equation("&Delta;t<sub>univ</sub>=h/(m<sub>e</sub>c<sup>2</sup>&alpha;<sub>PP</sub>), &nbsp; &Delta;x<sub>univ</sub>=c&Delta;t<sub>univ</sub>,", st),
        equation("&mu;<sub>M,FPM</sub>=(2/3)&zeta;/[(&alpha;<sub>PP</sub>+9)N<sup>4</sup>],", st),
        equation("G<sub>FPM</sub>=&mu;<sub>M,FPM</sub>&zeta;c<sup>4</sup>&Delta;x<sub>univ</sub>/J.", st),
        body("Equivalently, substitution gives G<sub>FPM</sub>=(2/3)&zeta;<sup>2</sup>hc<sup>3</sup>/[m<sub>e</sub>&alpha;<sub>PP</sub>(&alpha;<sub>PP</sub>+9)N<sup>5</sup>k<sub>B</sub>T<sub>bath</sub>ln2]. At T<sub>bath</sub>=300 K the map returns", st),
        equation("G<sub>FPM</sub>=6.68034009&times;10<super>-11</super> m<sup>3</sup> kg<super>-1</super> s<super>-2</super>,", st),
        body("compared with the CODATA value 6.67430(15)&times;10<sup>-11</sup> in the same units [13], a relative difference of about 0.0905 percent. This numerical proximity is exact for the implemented map, but the temperature is part of the dimensional calibration. A fundamental gravitational bridge must derive the relevant substrate temperature or replace it with a state variable whose transformation and cosmological evolution are fixed.", st),

        h1("5. Time dilation as finite processor lag", st),
        body("Let L_rest be the per-tick action required to maintain a reference process and L the action under gravitational or motion-induced load. FPM identifies their ratio with an effective lag factor", st),
        equation("&gamma;<sub>FPM</sub>=L/L<sub>rest</sub>, &nbsp;&nbsp; v<sub>eff</sub>=c L<sub>rest</sub>/L.", st),
        body("The same finite budget therefore links gravitational and motion-induced slowing: additional routing work leaves less causal capacity for internal evolution. Because the action law is bounded, the reference construction has a finite ratio", st),
        equation("1 &le; &gamma;<sub>FPM</sub> &le; &gamma;<sub>max</sub>=31.8738629.", st),
        body("This ceiling is a sharp prediction only for an observable demonstrably represented by L/L_rest. It is not a claim that every conventional Lorentz factor in every experimental context must stop at this number. The decisive work is to define the clock, particle, or transition observable from the carrier dynamics and then test the entire redshift or lifetime curve.", st),
        statement("Status", "The shared-budget explanation is constitutive; the numerical ceiling follows exactly from the selected action bounds. Its physical force depends on completing the observable map before comparison with high-lag data.", st),

        h1("6. Cosmology and acoustic structure", st),
        h2("6.1 Common boot state", st),
        body("FPM replaces the need for distant regions to negotiate their initial uniformity with a common pre-execution state. A finite substrate can begin from one prepared condition, just as independently addressed storage blocks can share a format because they were initialized together. This is a proposed initial-condition mechanism, not superluminal communication between later regions.", st),
        h2("6.2 Acoustic bridge", st),
        body("The numerical audit evaluates a compact algebraic spectrum rather than evolving a complete Boltzmann hierarchy. Its bridge function is", st),
        equation("S(&ell;)=A<sub>FPM</sub>(&ell;/&ell;<sub>A</sub>)<super>n<sub>s</sub>-1</super> exp[-(&ell;/&ell;<sub>D</sub>)<sup>2</sup>] {1+A<sub>osc</sub> sin<sup>2</sup>(&ell;/&ell;<sub>osc</sub>)}.", st),
        body("The fixed quantities include A<sub>FPM</sub>=4.0390&times;10<sup>-5</sup>, n<sub>s</sub>=0.9686263, tensor ratio r=0.00348596, damping scale ell<sub>D</sub>=1309.5688, acoustic scale ell<sub>A</sub>=299.82, and the declared ledger-inertia ratio 16/3. The compact template additionally sets A<sub>osc</sub>=0.6 and ell<sub>osc</sub>=80. Those two oscillation parameters are fixed constitutive template inputs: they are not derived by Papers 1-4 and the runtime does not estimate them from a likelihood. Their selection history does not support treating the present spectrum as an independent prediction. The present result is therefore an audited phenomenological correspondence whose replacement by transfer dynamics is part of the complete CMB test.", st),
        body("Against the selected Planck comparison [9], the existing fixed-nuisance audit reports Delta chi-squared = +4.16 relative to the Lambda-CDM reference. The positive value means the compact FPM bridge is somewhat worse in that comparison. Its importance is that a low-dimensional route-cost construction reaches the correct qualitative regime and exposes a complete next calculation: implement the transfer functions, polarization, lensing, covariance, foreground nuisance model, and a pre-committed likelihood protocol.", st),
        h2("6.3 Tensor suppression", st),
        body("The bridge assigns one specific structural contraction of the nine-channel ledger to the tensor contribution, producing a one-in-nine suppression rule. This is a constitutive channel assignment, not a counting theorem: the 3 by 3 ledger has nine independent entries, while its trace is a contraction of three diagonal entries. A physical tensor derivation must connect that assignment to gauge-invariant perturbations and their propagation.", st),

        h1("7. Finite Born distribution", st),
        body("For normalized carrier amplitudes psi_a, FPM uses the Born-compatible weights p_a=|psi_a| squared [10] and realizes them with N finite microcells. Largest-remainder allocation returns integer counts n_a summing exactly to N, with each allocation error below one cell. For nine outcomes and the carrier capacity in Paper 3, the total-variation error is bounded by 3.10&times;10<sup>-9</sup>; the reported runtime error is 1.20&times;10<sup>-9</sup>.", st),
        equation("n<sub>a</sub>/N &rarr; |&psi;<sub>a</sub>|<sup>2</sup>, &nbsp;&nbsp; D<sub>TV</sub>&lt;m/(2N).", st),
        body("Pure phase rotation leaves the immediate weights unchanged. The current construction establishes finite realization in one selected channel basis. General detector orientation requires an explicit basis-change operation and contextual measurement map; that is the central extension needed before the bridge constitutes a general measurement theory.", st),

        h1("8. Joint torsion and Bell/CHSH correlations", st),
        h2("8.1 Explicit shared boundary", st),
        body("The FPM pair construction does not assign two independent local carriers prewritten answers. It quantizes a joint distribution across a shared torsion boundary. For detector settings a and b, the ideal correlation is", st),
        equation("E(a,b)=-cos[2(a-b)].", st),
        body("The four joint probabilities sum to one and leave each wing individually balanced at fifty-fifty. For the standard four settings, the CHSH combination reaches", st),
        equation("S=|E(a,b)+E(a,b')+E(a',b)-E(a',b')|=2sqrt(2).", st),
        body("The runtime's finite allocation reproduces the target within its microcell error. An independent local baseline produces the expected triangular correlation and remains at or below S=2.", st),
        statement("Locality classification", "The shared torsion boundary is a non-Bell-local resource. The construction therefore does not evade Bell's theorem or the CHSH formulation [11,12]; it selects a joint architecture outside Bell factorizability and must satisfy no-signalling, relativistic causal consistency, and an independently specified formation and decay law.", st),
        h2("8.2 Resource gate", st),
        body("FPM further proposes that the joint link survives only while the finite budget remains in the deep consolidation regime. As resource load changes, the model predicts a transition from the quantum value 2sqrt(2) toward the classical bound 2. This is more discriminating than reproducing the ideal quantum curve: the location, width, and control variable of the transition must be fixed from the same action ledger and tested without retuning.", st),

        h1("9. Bare electromagnetic coupling", st),
        body("The torsion-snap bridge uses two distinct floors that must not be conflated. The action floor is c<sub>0</sub>=0.05. The quantity e<sub>floor</sub>=0.0314 is instead the dimensionless structural percolation floor in the causal-depletion law", st),
        equation("e<sub>eff</sub>(B)=max[(1+B)<super>-3/4</super>,e<sub>floor</sub>].", st),
        body("Here B&ge;0 is the dimensionless local baryonic, or ordinary-matter, load supplied to the viscosity-energy gate; B=0 denotes no added matter load. It is a bridge input distinct from cache bias b, bit count B<sub>erase</sub>, and the action L.", st),
        body("Thus e<sub>floor</sub> is not c<sub>0</sub>/E<sub>max</sub>, which equals 0.075. With the symmetric-sector exponent beta=9/5, the maximum symmetric occupancy is", st),
        equation("C<sub>sym,max</sub>=(1/e<sub>floor</sub>)<super>1/&beta;</super>, &nbsp;&nbsp; &alpha;<sub>bare</sub>=c<sub>0</sub>/C<sub>sym,max</sub>.", st),
        body("Using the shared FPM constants gives inverse alpha_bare = 136.7946397586. The CODATA inverse fine-structure constant is approximately 137.036 [13]; the difference is about 0.1761 percent. FPM interprets its number as a bare coupling before vacuum screening, not as the macroscopic measured value itself. The physical programme is therefore to derive the screening correction from carrier excitations rather than choosing a correction after comparison.", st),
        body("The proposed excitation is a paid, trace-free transverse disturbance released when a shared topological link can no longer be maintained. The decomposition of the 3 by 3 ledger into antisymmetric and symmetric sectors supplies three circulation-like and six strain-like components. Connecting this structure to a massless spin-one gauge field, charge conservation, polarization, and quantum electrodynamic running remains the decisive field-theory derivation.", st),
        statement("Status", "The bare number is an exact output of the selected upstream constants. Establishing independence from the target requires sensitivity analysis and a derivation whose choices are fixed before comparison with alpha.", st),

        h1("10. Shared dependency and empirical risk", st),
        body("The bridges are coupled through route cost. This is the framework's central economy and its strongest vulnerability. A failure of the local ledger or viscosity law propagates into gravity, time dilation, cosmology, and the coupling construction; a failure unique to a detector map need not invalidate local conservation or the finite carrier.", st),
        bullet("<b>Ledger layer:</b> locality, signed conservation, and finite support are shared by every bridge.", st),
        bullet("<b>Constitutive layer:</b> viscosity endpoints and exponents jointly affect gravity, lag, and several reported constants.", st),
        bullet("<b>Carrier layer:</b> normalization, phase, consolidation, and finite allocation jointly affect Born, Bell, and Landauer results.", st),
        bullet("<b>Dimensional layer:</b> temperature and unit maps affect the numerical values of G and mass-equivalent scales.", st),
        bullet("<b>Observable layer:</b> SPARC source functions, cosmological transfer functions, detector bases, and screening maps can fail independently.", st),
        h2("10.1 Highest-value next tests", st),
        bullet("Predict full two-dimensional galaxy velocity fields and lensing from the tensor ledger, with one frozen parameter set.", st),
        bullet("Run a complete CMB temperature, polarization, lensing, covariance, and foreground likelihood with the bridge fixed in advance.", st),
        bullet("Derive a concrete clock or particle observable for gamma_FPM and test the entire curve through the predicted ceiling regime.", st),
        bullet("Specify the resource variable controlling joint torsion and test the predicted CHSH transition while preserving no-signalling.", st),
        bullet("Derive electromagnetic screening and scale dependence from the same carrier rather than importing the measured correction.", st),

        h1("11. Conclusion", st),
        body("FPM's bridge programme is now stated as an auditable dependency stack. The framework reproduces selected mathematical forms for dephasing, finite probability allocation, joint quantum correlations, action-lag ratios, and several fixed algebraic constructions. It retains calibrated and correspondence-level numerical comparisons in cosmology, gravitation, and electromagnetic coupling, plus archived but unregenerated galaxy-benchmark metadata. None of these results stands alone: their scientific value comes from a common route-cost mechanism and from the possibility of testing that mechanism across regimes with one declared parameter ledger.", st),
        statement("Central conclusion", "The physical claim is not that resemblance proves identity. It is that one finite local accounting system generates a tightly linked set of quantitative correspondences, and that the links are now precise enough to expose clean failure conditions.", st),

        PageBreak(),
        h1("References", st),
        reference("[1] A. Spiker, <i>FPM Foundations</i>, Modular Paper 01, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21420508'>https://doi.org/10.5281/zenodo.21420508</a>", st),
        reference("[2] A. Spiker, <i>Executable FPM</i>, Modular Paper 02, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21420643'>https://doi.org/10.5281/zenodo.21420643</a>", st),
        reference("[3] A. Spiker, <i>Finite Carrier and Information Dynamics</i>, Modular Paper 03, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21420648'>https://doi.org/10.5281/zenodo.21420648</a>", st),
        reference("[4] A. Spiker, <i>Tensorless Exact-Ledger Sandbox</i>, Modular Paper 04, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21420650'>https://doi.org/10.5281/zenodo.21420650</a>", st),
        reference("[5] G. Lindblad, “On the Generators of Quantum Dynamical Semigroups,” <i>Communications in Mathematical Physics</i> 48, 119–130 (1976). <a href='https://doi.org/10.1007/BF01608499'>https://doi.org/10.1007/BF01608499</a>", st),
        reference("[6] R. Landauer, “Irreversibility and Heat Generation in the Computing Process,” <i>IBM Journal of Research and Development</i> 5, 183–191 (1961). <a href='https://doi.org/10.1147/rd.53.0183'>https://doi.org/10.1147/rd.53.0183</a>", st),
        reference("[7] M. Milgrom, “A Modification of the Newtonian Dynamics as a Possible Alternative to the Hidden Mass Hypothesis,” <i>Astrophysical Journal</i> 270, 365–370 (1983). <a href='https://doi.org/10.1086/161130'>https://doi.org/10.1086/161130</a>", st),
        reference("[8] F. Lelli, S. S. McGaugh, and J. M. Schombert, “SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves,” <i>Astronomical Journal</i> 152, 157 (2016). <a href='https://doi.org/10.3847/0004-6256/152/6/157'>https://doi.org/10.3847/0004-6256/152/6/157</a>", st),
        reference("[9] Planck Collaboration, “Planck 2018 Results. VI. Cosmological Parameters,” <i>Astronomy & Astrophysics</i> 641, A6 (2020); correction 652, C4 (2021). <a href='https://doi.org/10.1051/0004-6361/201833910'>https://doi.org/10.1051/0004-6361/201833910</a>", st),
        reference("[10] M. Born, “Zur Quantenmechanik der Stoßvorgänge,” <i>Zeitschrift für Physik</i> 37, 863–867 (1926). <a href='https://doi.org/10.1007/BF01397477'>https://doi.org/10.1007/BF01397477</a>", st),
        reference("[11] J. S. Bell, “On the Einstein Podolsky Rosen Paradox,” <i>Physics Physique Fizika</i> 1, 195–200 (1964). <a href='https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195'>https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195</a>", st),
        reference("[12] J. F. Clauser, M. A. Horne, A. Shimony, and R. A. Holt, “Proposed Experiment to Test Local Hidden-Variable Theories,” <i>Physical Review Letters</i> 23, 880–884 (1969). <a href='https://doi.org/10.1103/PhysRevLett.23.880'>https://doi.org/10.1103/PhysRevLett.23.880</a>", st),
        reference("[13] E. Tiesinga, P. J. Mohr, D. B. Newell, and B. N. Taylor, “CODATA Recommended Values of the Fundamental Physical Constants: 2018,” <i>Reviews of Modern Physics</i> 93, 025010 (2021). <a href='https://doi.org/10.1103/RevModPhys.93.025010'>https://doi.org/10.1103/RevModPhys.93.025010</a>", st),
        reference("[14] A. Spiker, <i>Finite Possibility Mechanics: A Unified Information-Theoretic Framework</i>, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21352386'>https://doi.org/10.5281/zenodo.21352386</a>", st),
        reference("[15] A. Spiker, <i>Finite Possibility Mechanics Complete</i>, source repository, <a href='https://github.com/alxspiker/Finite-Possibility-Mechanics-Complete'>https://github.com/alxspiker/Finite-Possibility-Mechanics-Complete</a> (accessed July 2026).", st),
    ]
    return s


if __name__ == "__main__":
    print(build_manuscript(SPEC, manuscript))
