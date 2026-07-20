#!/usr/bin/env python3
"""Generate Modular Paper 01: FPM Foundations."""

from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, Spacer, Table, TableStyle

from _paper_template import (
    GOLD,
    INK,
    MUTED,
    NAVY,
    PaperSpec,
    body,
    build_manuscript,
    bullet,
    equation,
    h1,
    h2,
    reference,
    statement,
)


SPEC = PaperSpec(
    number=1,
    title="FPM Foundations",
    subtitle="Finite Local Substrates, Directed Route Ledgers, and Exact Closure",
    filename="01_FPM_Foundations.pdf",
    scope="A self-contained axiomatic and mathematical foundation for Finite Possibility Mechanics.",
    claim_boundary="The paper proves the finite-graph results used by the remainder of the FPM research series.",
    sections=[
        ("Abstract", "Principal construction and exact results."),
        ("Finite possibility as a mechanics", "The organizing problem and architecture."),
        ("Axioms and state space", "The five axioms and finite periodic substrate."),
        ("Directed route ledger", "Nine route channels, invariant contractions, and decomposition."),
        ("Constitutive mobility and viscosity", "Explicit constitutive definitions and their bounds."),
        ("Local replenishment kernel", "Nearest-neighbour transport, stochasticity, and detailed balance."),
        ("Exact closure theorems", "Global, local, regional, causal, and equilibrium results."),
        ("Finite action and causal order", "Finite work capacity and order sensitivity."),
        ("Geometric closure", "Exact antisymmetric route forms on closed boundaries."),
        ("Continuum scaling", "Conditional finite-volume limit."),
        ("Dependency structure", "What is defined, proved, and passed to later papers."),
        ("Conclusion", "Foundational result."),
        ("References", "Primary and archival sources."),
    ],
    document_label="FOUNDATIONS PAPER",
)


def table(rows, widths, styles, header=True):
    body_style = styles["BodyFPM"].clone("TableBodyFPM")
    body_style.fontSize = 8.5
    body_style.leading = 10.6
    body_style.spaceBefore = 0
    body_style.spaceAfter = 0
    body_style.textColor = INK

    header_style = styles["ManuscriptH2"].clone("TableHeaderFPM")
    header_style.fontSize = 8.5
    header_style.leading = 10.6
    header_style.spaceBefore = 0
    header_style.spaceAfter = 0
    header_style.textColor = colors.white

    wrapped_rows = []
    for row_index, row in enumerate(rows):
        cell_style = header_style if header and row_index == 0 else body_style
        wrapped_rows.append([
            Paragraph(cell, cell_style) if isinstance(cell, str) else cell
            for cell in row
        ])

    t = Table(wrapped_rows, colWidths=widths, repeatRows=1 if header else 0, hAlign="LEFT")
    commands = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#C9D3DE")),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
        ("FONTNAME", (0, 0), (-1, -1), styles["BodyFPM"].fontName),
        ("FONTSIZE", (0, 0), (-1, -1), 8.5),
        ("TEXTCOLOR", (0, 0), (-1, -1), INK),
    ]
    if header:
        commands.extend([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("FONTNAME", (0, 0), (-1, 0), styles["ManuscriptH2"].fontName),
        ])
    t.setStyle(TableStyle(commands))
    return t


def manuscript(styles):
    s = []

    s += [
        h1("Abstract", styles),
        body(
            "Finite Possibility Mechanics (FPM) is a mechanics of directed alternatives under finite memory, finite energy, and finite update time. Its primitive object is a local directed route ledger carried by the sites of a finite periodic cubic lattice. A positive per-tick route cost is transported through a nearest-neighbour Markov kernel and recorded in a closed signed energy ledger. This paper gives the model a precise finite-graph foundation and proves the results on which the later carrier, exact-ledger, physical-bridge, and empirical papers depend.",
            styles,
        ),
        body(
            "The principal results are exact. The local transport matrix is non-negative, row-stochastic, reversible with respect to the activity measure, and supported only on graph edges and self-loops. Replenishment therefore conserves total interior energy, admits an antisymmetric edge-flux representation, satisfies nodewise and regional continuity, and propagates support by at most one graph edge per tick. Under frozen positive weights on a connected lattice, repeated local transport converges to the activity-weighted distribution; the earlier globally normalized replenishment formula is recovered as this equilibrium limit, not as an instantaneous transfer rule. A positive action floor also gives a finite upper bound on the number of operations executable from any finite budget. These statements establish a closed, causal, finite substrate without appealing to a continuum approximation.",
            styles,
        ),
        statement(
            "Foundational result",
            "FPM's ordinary interior dynamics is an exactly conservative local transport system. Capacity saturation, starvation, paid erasure, and declared structural operations are incorporated by additional signed ledger terms rather than hidden inside the interior transport law.",
            styles,
        ),
        Spacer(1, 4 * mm),
        body("<b>Record DOI:</b> <a href='https://doi.org/10.5281/zenodo.21420508'>https://doi.org/10.5281/zenodo.21420508</a>", styles),
        body("<b>Keywords:</b> finite information dynamics; directed routing; local conservation; Markov transport; discrete continuity; finite causal cone; exact ledger", styles),
    ]

    s += [
        h1("1. Finite possibility as a mechanics", styles),
        body(
            "A physical or computational system can distinguish only the alternatives represented in its state, can update only by spending available action, and can transmit influence only through available routes. FPM begins by treating those three limitations as a single mechanical problem. Possibilities are not an unpriced list external to the system. They are represented by finite local state, maintained by finite energy, and changed by ordered operations.",
            styles,
        ),
        body(
            "The central variable is therefore not a probability distribution alone, but a <i>directed route ledger</i>: a local record of how costly it is to carry state from one directional channel into another. This ledger determines a mobility, mobility determines a viscosity, viscosity enters the per-tick action, and the action is debited and replenished through a closed local transport rule. Later papers add the complex carrier, information-erasure dynamics, exact integer realization, physical correspondences, and empirical tests. The present paper establishes the common mathematical core.",
            styles,
        ),
        h2("1.1 The foundational chain", styles),
        equation(
            "finite substrate &rarr; directed route ledger &rarr; mobility and viscosity &rarr; per-tick action &rarr; local replenishment &rarr; next state",
            styles,
        ),
        body(
            "Each arrow is a declared map. This matters: a theory is auditable only when definitions, constitutive selections, and derived consequences are not blended together. FPM uses axioms to define the admissible state and update structure, constitutive laws to select one dynamics from that admissible class, and theorems to establish what the selected dynamics necessarily does.",
            styles,
        ),
        h2("1.2 Three levels of statement", styles),
        table([
            ["Level", "Role in FPM", "Examples in this paper"],
            ["Axiom", "Defines admissible mechanics", "Substrate; route cost; ledger; ticks; calibration"],
            ["Constitutive", "Selects one admissible dynamics", "Mobility; viscosity; local kernel"],
            ["Theorem", "Follows from prior definitions", "Stochasticity; balance; continuity; causality"],
        ], [28 * mm, 58 * mm, 68 * mm], styles),
    ]

    s += [
        h1("2. Axioms and state space", styles),
        h2("2.1 A1 — Finite local substrate", styles),
        statement(
            "Axiom A1 (Finite local substrate)",
            "The system occupies a finite, locally connected graph. For the cubic realization, the vertex set is the periodic quotient &Lambda;<sub>n</sub> = (Z/nZ)<sup>3</sup> with n &ge; 3. Every vertex has six nearest neighbours. Each vertex stores finite energy, a finite directed route ledger, and finite auxiliary state.",
            styles,
        ),
        body(
            "The periodic lattice is a finite discrete three-torus. It preserves the six-neighbour local geometry of the cubic lattice while removing an artificial outer boundary from the interior transport experiment. The infinite lattice Z<sup>3</sup> is the covering geometry; the executable object is its finite periodic quotient.",
            styles,
        ),
        equation("|&Lambda;<sub>n</sub>| = n<sup>3</sup>, &nbsp;&nbsp; deg(i) = 6, &nbsp;&nbsp; (i,j) is an edge iff i and j differ by one periodic lattice step", styles),
        h2("2.2 A2 — Positive thermodynamic route cost", styles),
        statement(
            "Axiom A2 (Positive route cost)",
            "Every executed route operation has a non-negative action cost. An executed non-null operation pays at least c<sub>0</sub> &gt; 0, and a tick has a finite action ceiling L<sub>max</sub> &lt; &infin;.",
            styles,
        ),
        body(
            "The action floor is what converts finite energy into a finite operation count. The detailed operational cost function and its integer representation belong to Papers 2 and 4; the foundational result requires only positivity and boundedness.",
            styles,
        ),
        statement(
            "Currency convention",
            "E<sub>i,t</sub> and L<sub>i,t</sub> use the same normalized energy-budget unit. L<sub>i,t</sub> is the energy debit accumulated by route operations during one discrete tick; the executable papers call it per-tick action as shorthand. After physical calibration, the corresponding dimensionful action is S<sub>i,t</sub>=L<sub>i,t</sub>E<sub>unit</sub>&Delta;t. The ledger therefore subtracts energy from energy, never dimensionful action from energy.",
            styles,
        ),
        h2("2.3 A3 — Closed signed ledger", styles),
        statement(
            "Axiom A3 (Closed signed ledger)",
            "No energy appears without a declared ledger source and no energy disappears without a declared ledger sink. Ordinary replenishment redistributes paid action internally. Capacity exhaust, starvation deficits, information-erasure debits, and explicit structural transfers occupy separate signed accounts.",
            styles,
        ),
        body(
            "This axiom does not require stored energy alone to remain constant under every branch. It requires the expanded signed account to close. That distinction is essential whenever a finite-capacity state is clipped or an operation is only partially affordable.",
            styles,
        ),
        h2("2.4 A4 — Discrete causal ticks", styles),
        statement(
            "Axiom A4 (Discrete causal ticks)",
            "State evolves through an ordered sequence t = 0,1,2,... . During one ordinary transport tick, information and replenishment may traverse at most one graph edge. Update order is part of the state-transition rule.",
            styles,
        ),
        h2("2.5 A5 — Physical propagation calibration", styles),
        statement(
            "Axiom A5 (Physical calibration)",
            "The fastest admissible propagation mode of the substrate is identified with the vacuum speed of light c. If one lattice edge has physical length &Delta;x and one tick has duration &Delta;t, then &Delta;x = c&Delta;t.",
            styles,
        ),
        body(
            "A1–A4 define the dimensionless mechanics. A5 supplies the physical unit bridge. The separate calibration paper determines any proposed numerical value of &Delta;x or &Delta;t; no such value is needed for the finite-graph theorems proved here.",
            styles,
        ),
        h2("2.6 Local state", styles),
        equation(
            "X<sub>i,t</sub> = (E<sub>i,t</sub>, R<sub>i,t</sub>, &xi;<sub>i,t</sub>), &nbsp;&nbsp; 0 &le; E<sub>i,t</sub> &le; E<sub>max</sub>, &nbsp;&nbsp; R<sub>i,t</sub> in R<sup>3&times;3</sup>",
            styles,
        ),
        body(
            "Here E<sub>i,t</sub> is stored energy, R<sub>i,t</sub> is the directed route ledger, and &xi;<sub>i,t</sub> denotes finite auxiliary state. The auxiliary state includes the fallback prior &pi;<sub>i,t</sub> and local target &tau;<sub>i,t</sub> used by the activity law below. Paper 3 further resolves &xi; into the nine-channel complex carrier, phase, prior, target, and consolidation variables. Keeping the remaining structure abstract here shows which closure results depend only on locality and accounting.",
            styles,
        ),
    ]

    s += [
        h1("3. Directed route ledger", styles),
        h2("3.1 Nine directed channels", styles),
        body(
            "At each site, R<sub>ab</sub> records the burden of transferring state from incoming spatial direction a to outgoing spatial direction b, with a,b in {x,y,z}. There are exactly 3&times;3 = 9 ordered directional pairs. Directionality permits R<sub>ab</sub> &ne; R<sub>ba</sub>.",
            styles,
        ),
        equation(
            "R = [[R<sub>xx</sub>, R<sub>xy</sub>, R<sub>xz</sub>], [R<sub>yx</sub>, R<sub>yy</sub>, R<sub>yz</sub>], [R<sub>zx</sub>, R<sub>zy</sub>, R<sub>zz</sub>]]",
            styles,
        ),
        statement(
            "Proposition 1 (Channel count)",
            "A directed linear map between three spatial route axes has nine independent coordinate entries. The trace is one scalar contraction of those nine entries; it is not a tenth independent degree of freedom.",
            styles,
        ),
        body(
            "This distinction makes the bookkeeping exact. FPM's 9:1 mobility weighting compares the full nine-entry route burden with one distinguished scalar contraction. It is a constitutive weighting convention, not a claim that a 3&times;3 matrix contains ten independent coordinates.",
            styles,
        ),
        h2("3.2 Symmetric and antisymmetric decomposition", styles),
        equation(
            "R = S + A, &nbsp;&nbsp; S = (R + R<super>T</super>)/2, &nbsp;&nbsp; A = (R - R<super>T</super>)/2",
            styles,
        ),
        statement(
            "Proposition 2 (Unique route decomposition)",
            "Every real 3&times;3 route ledger has a unique decomposition into a symmetric ledger S and an antisymmetric ledger A. S has six independent components, A has three, and their Frobenius inner product is zero.",
            styles,
        ),
        body(
            "Proof. Transposition gives S<super>T</super>=S and A<super>T</super>=-A. Their sum is R. If R=S<sub>1</sub>+A<sub>1</sub>=S<sub>2</sub>+A<sub>2</sub>, then S<sub>1</sub>-S<sub>2</sub>=-(A<sub>1</sub>-A<sub>2</sub>) is both symmetric and antisymmetric, hence zero. Finally tr(S<super>T</super>A)=tr(SA)=-tr(SA)=0. QED.",
            styles,
        ),
        h2("3.3 Scalar invariants", styles),
        equation("S<sub>9</sub>(R) = [ (1/9) &Sigma;<sub>a,b</sub> R<sub>ab</sub><sup>2</sup> ]<sup>1/2</sup>", styles),
        equation("K<sub>1</sub>(R) = |tr(R)| = |R<sub>xx</sub> + R<sub>yy</sub> + R<sub>zz</sub>|", styles),
        body(
            "S<sub>9</sub> measures the root-mean-square burden across all directed channels. K<sub>1</sub> extracts the magnitude of the isotropic trace channel. Both are non-negative and invariant under simultaneous orthogonal changes of the spatial basis: R &mapsto; QRQ<super>T</super>.",
            styles,
        ),
        statement(
            "Proposition 3 (Basis invariance)",
            "For orthogonal Q, S<sub>9</sub>(QRQ<super>T</super>)=S<sub>9</sub>(R) and K<sub>1</sub>(QRQ<super>T</super>)=K<sub>1</sub>(R).",
            styles,
        ),
        body(
            "Proof. The Frobenius norm is invariant under orthogonal left and right multiplication, and trace is invariant under similarity transformations. QED.",
            styles,
        ),
    ]

    s += [
        h1("4. Constitutive mobility and viscosity", styles),
        h2("4.1 Mobility map", styles),
        body(
            "The route invariants become dynamical through a constitutive mobility. FPM selects the normalized map",
            styles,
        ),
        equation("&Phi;<sub>&Omega;</sub>(R) = A<sub>0</sub>(1+K<sub>1</sub>)<sup>&alpha;</sup> / (1+S<sub>9</sub>)<sup>&beta;</sup>", styles),
        body(
            "where A<sub>0</sub>&gt;0 fixes the dimensionless normalization. The FPM weighting convention contains two choices. The 1:9 ratio fixes the relative sensitivity assigned to one distinguished trace contraction and the nine entries of the directed ledger. The condition &alpha;+&beta;=2 fixes the remaining common exponent scale by selecting a quadratic response order:",
            styles,
        ),
        equation("&alpha; = 2/(1+9) = 1/5, &nbsp;&nbsp; &beta; = 18/(1+9) = 9/5", styles),
        statement(
            "Constitutive selection C1 (Trace-to-ledger weighting)",
            "FPM weights one trace contraction against the nine-entry directed ledger and chooses total exponent order two. These two constitutive choices select (&alpha;,&beta;)=(1/5,9/5).",
            styles,
        ),
        body(
            "The total order two is not a theorem of cubic geometry. Without it, the 1:9 ratio leaves one free common exponent scale; C1 fixes that response stiffness at the quadratic order selected by the route-cost model. Alternative total orders define alternative constitutive models and must be compared by sensitivity and empirical tests. Once C1 is selected, positivity and monotonicity are exact: &Phi;<sub>&Omega;</sub>&gt;0; increasing K<sub>1</sub> at fixed S<sub>9</sub> increases mobility; increasing S<sub>9</sub> at fixed K<sub>1</sub> decreases it.",
            styles,
        ),
        h2("4.2 Bounded viscosity", styles),
        equation("C<sub>t</sub> = min(A<sub>t</sub>,1), &nbsp;&nbsp; &kappa;<sub>t</sub> = C<sub>t</sub> g(e<sub>t</sub>), &nbsp;&nbsp; 0 &le; g(e) &le; 1", styles),
        equation("&Omega;<sub>t</sub> = &Omega;<sub>max</sub> - (&Omega;<sub>max</sub>-&Omega;<sub>min</sub>)&kappa;<sub>t</sub>", styles),
        statement(
            "Proposition 4 (Viscosity bound)",
            "If 0&le;C<sub>t</sub>&le;1 and 0&le;g(e<sub>t</sub>)&le;1, then &Omega;<sub>min</sub>&le;&Omega;<sub>t</sub>&le;&Omega;<sub>max</sub> at every tick.",
            styles,
        ),
        body(
            "Proof. The product &kappa;<sub>t</sub> lies in [0,1]. The viscosity equation is the affine image of that interval, with endpoints &Omega;<sub>max</sub> and &Omega;<sub>min</sub>. QED.",
            styles,
        ),
        body(
            "The numerical endpoint choices and the energy-gate exponent are constitutive parameters of the executable realization. Paper 2 records them with their derivation history and sensitivity tests. The foundational theorem requires only their admissible ranges.",
            styles,
        ),
    ]

    s += [
        h1("5. Local replenishment kernel", styles),
        h2("5.1 Activity and symmetric edge mobility", styles),
        body(
            "Let G=(V,E) be a finite undirected graph with maximum degree d<sub>max</sub>. At tick t, each vertex has positive activity weight w<sub>i,t</sub>&gt;0. Each edge has a symmetric mobility gate 0&lt;&mu;<sub>ij,t</sub>=&mu;<sub>ji,t</sub>&le;1. In the cubic FPM realization, d<sub>max</sub>=6 and the gate is computed from endpoint viscosities:",
            styles,
        ),
        equation("&mu;<sub>ij,t</sub> = 1 - [&Omega;<sub>i,t</sub> + &Omega;<sub>j,t</sub>]/2", styles),
        body(
            "For the public reference dynamics, activity is a local function of route-ledger dispersion and prior-target mismatch. Define",
            styles,
        ),
        equation("m<sub>R,i,t</sub> = (1/9)&Sigma;<sub>a,b</sub>R<sub>ab,i,t</sub>", styles),
        equation("&sigma;<sub>R,i,t</sub> = sqrt{(1/9)&Sigma;<sub>a,b</sub>[R<sub>ab,i,t</sub>-m<sub>R,i,t</sub>]<sup>2</sup>}", styles),
        equation("w<sub>i,t</sub> = max(&epsilon;<sub>w</sub>, &sigma;<sub>R,i,t</sub> + &eta;<sub>geo</sub>|&pi;<sub>i,t</sub>-&tau;<sub>i,t</sub>|)", styles),
        body(
            "Here m<sub>R,i,t</sub> is the arithmetic mean of the nine directed entries of R<sub>i,t</sub>. The symbol &pi;<sub>i,t</sub> denotes the site-local fallback prior stored by the runtime; it is not the stationary distribution of the transport kernel.",
            styles,
        ),
        statement(
            "Constitutive selection C2 (Local activity)",
            "The reference runtime uses &eta;<sub>geo</sub>=0.1 and &epsilon;<sub>w</sub>=10<super>-9</super>. Thus w<sub>i,t</sub> is computed entirely from the local state X<sub>i,t</sub>; it is not an external global weight.",
            styles,
        ),
        body(
            "Theorems 1–7 require only finite positive weights and therefore remain valid for other declared local activity laws. C2 identifies the particular law executed by Paper 2 and closes the foundational state-to-kernel chain.",
            styles,
        ),
        h2("5.2 Metropolis-type transition rule", styles),
        equation("P<sub>ij,t</sub> = (&mu;<sub>ij,t</sub>/d<sub>max</sub>) min(1,w<sub>j,t</sub>/w<sub>i,t</sub>) &nbsp; for j in N(i)", styles),
        equation("P<sub>ii,t</sub> = 1 - &Sigma;<sub>j in N(i)</sub>P<sub>ij,t</sub>, &nbsp;&nbsp; P<sub>ij,t</sub>=0 otherwise", styles),
        body(
            "This is a local reversible transition rule in the Metropolis family [1,2]. The self-loop stores the probability not assigned to neighbour transfers; physically, it represents route cost that remains at its source during the tick.",
            styles,
        ),
        statement(
            "Theorem 1 (Admissible local kernel)",
            "P<sub>t</sub> is non-negative, row-stochastic, and supported on graph edges and self-loops.",
            styles,
        ),
        body(
            "Proof. For an edge, every factor in P<sub>ij,t</sub> is non-negative and P<sub>ij,t</sub>&le;1/d<sub>max</sub>. Vertex i has at most d<sub>max</sub> neighbours, hence &Sigma;<sub>j in N(i)</sub>P<sub>ij,t</sub>&le;1 and P<sub>ii,t</sub>&ge;0. The definition of P<sub>ii,t</sub> makes each row sum exactly one. Off-edge entries vanish by definition. QED.",
            styles,
        ),
        statement(
            "Theorem 2 (Detailed balance)",
            "The kernel is reversible with respect to the positive activity measure: w<sub>i,t</sub>P<sub>ij,t</sub>=w<sub>j,t</sub>P<sub>ji,t</sub> for every edge.",
            styles,
        ),
        body(
            "Proof. Symmetry of &mu; gives w<sub>i</sub>P<sub>ij</sub>=(&mu;<sub>ij</sub>/d<sub>max</sub>)min(w<sub>i</sub>,w<sub>j</sub>)=w<sub>j</sub>P<sub>ji</sub>. QED.",
            styles,
        ),
        equation("&rho;<sub>i,t</sub><super>eq</super> = w<sub>i,t</sub>/W<sub>t</sub>, &nbsp;&nbsp; W<sub>t</sub>=&Sigma;<sub>k</sub>w<sub>k,t</sub>", styles),
        body(
            "Detailed balance immediately yields stationarity: P<sub>t</sub><super>T</super>&rho;<sub>t</sub><super>eq</super>=&rho;<sub>t</sub><super>eq</super>. The normalized vector &rho;<sub>t</sub><super>eq</super> is an observer-level description of the frozen kernel's equilibrium; computing it is not part of the local one-tick transport update.",
            styles,
        ),
        h2("5.3 Route-temperature canonicality boundary", styles),
        body(
            "Detailed balance identifies an equilibrium activity potential, not a thermodynamic temperature. On a connected active undirected graph, define g<sub>ij</sub>=ln(P<sub>ij</sub>/P<sub>ji</sub>) and d<sub>ij</sub>=L<sub>j</sub>-L<sub>i</sub> on every edge. Theorem 2 gives g<sub>ij</sub>=ln(w<sub>j</sub>/w<sub>i</sub>). A scalar canonical route-temperature law would require the additional relation g<sub>ij</sub>=-&beta;<sub>L</sub>d<sub>ij</sub> on every edge, with &beta;<sub>L</sub>=epsilon<sub>L</sub>/(k<sub>B</sub>T)&gt;0 only after a positive energy-per-route dictionary epsilon<sub>L</sub> is supplied.",
            styles,
        ),
        statement(
            "Route-temperature canonicality boundary",
            "The local kernel derives the activity potential -ln(w<sub>i</sub>). It does not derive a Boltzmann relation between that potential and route cost L<sub>i</sub>.",
            styles,
        ),
        body(
            "Proof. Theorem 2 fixes only the ratio P<sub>ij</sub>/P<sub>ji</sub>=w<sub>j</sub>/w<sub>i</sub>. Neither the transition rule nor Axioms A1-A5 imposes ln(w<sub>j</sub>/w<sub>i</sub>)=-&beta;<sub>L</sub>(L<sub>j</sub>-L<sub>i</sub>). Thus the latter is an independent state-law condition, which can be tested edge by edge. QED.",
            styles,
        ),
        body(
            "The criterion is necessary and sufficient on that connected graph: g<sub>ij</sub>=-&beta;<sub>L</sub>d<sub>ij</sub> on every edge if and only if ln(w<sub>i</sub>)=C-&beta;<sub>L</sub>L<sub>i</sub>, equivalently &rho;<sub>i</sub><super>eq</super> is proportional to exp(-&beta;<sub>L</sub>L<sub>i</sub>). If route cost is nonconstant, &beta;<sub>L</sub> is unique and its unweighted least-squares value is -(d dot g)/(d dot d); the relation holds exactly when g+&beta;<sub>L</sub>d=0 on every edge. If d=0 on every edge, connectedness makes g=0 equivalent to uniform activity and leaves &beta;<sub>L</sub> unidentifiable; nonuniform activity rules out every scalar relation. A positive finite Kelvin temperature additionally requires &beta;<sub>L</sub>&gt;0 and a separately supplied positive epsilon<sub>L</sub>.",
            styles,
        ),
        body(
            "For the declared first master-chain action state (5<sup>3</sup> sites, seed 17, torsion initialization, then the tick-zero truth-target update before replenishment), the unweighted 375-edge least-squares estimate is &beta;<sub>L</sub>=-0.0019023970513 and the normalized incompatibility ||g+&beta;<sub>L</sub>d||<sub>2</sub>/||g||<sub>2</sub>=0.999993565405. The raw detailed-balance flux residual max|w<sub>i</sub>P<sub>ij</sub>-w<sub>j</sub>P<sub>ji</sub>| is 1.73x10<sup>-18</sup>; separately, the maximum log-ratio activity-potential residual max|g-ln(w<sub>j</sub>/w<sub>i</sub>)| is 2.22x10<sup>-16</sup>. Two edges alone witness non-collinearity: (5,9) gives -g/d=-0.1600522947 and (67,72) gives 0.9768490669, with determinant g<sub>1</sub>d<sub>2</sub>-g<sub>2</sub>d<sub>1</sub>=-4.5512145855x10<sup>-4</sup>. The declared state therefore admits no scalar canonical temperature conjugate to L. This does not prohibit a separately postulated thermodynamic state law or a different energy observable.",
            styles,
        ),
        h2("5.4 Exact homogeneous cubic spectrum", styles),
        body(
            "Fix a periodic cubic lattice of side n, constant activity w<sub>i</sub>=w<sub>0</sub>, and constant viscosity &Omega;<sub>i</sub>=&Omega;<sub>0</sub>. Write &mu;=1-&Omega;<sub>0</sub>. The transport operator is then translation invariant and symmetric:",
            styles,
        ),
        equation("(PL)<sub>x</sub>=(1-&mu;)L<sub>x</sub>+(&mu;/6)&Sigma;<sub>|e|=1</sub>L<sub>x+e</sub>", styles),
        statement(
            "Homogeneous-spectrum theorem",
            "For k<sub>a</sub>=2&pi;m<sub>a</sub>/(n&Delta;x), m<sub>a</sub> in {0,...,n-1}, every Fourier character exp(i k dot x) is an exact eigenvector with multiplier &lambda;(k)=1-&mu;+(&mu;/3)[cos(k<sub>x</sub>&Delta;x)+cos(k<sub>y</sub>&Delta;x)+cos(k<sub>z</sub>&Delta;x)].",
            styles,
        ),
        body(
            "Proof. Translation by &plusmn;&Delta;x along axis a multiplies a Fourier character by exp(&plusmn;ik<sub>a</sub>&Delta;x). Pairing the two neighbours gives 2cos(k<sub>a</sub>&Delta;x), and substitution in the six-neighbour rule gives the stated multiplier. The characters form the complete Fourier basis of the finite periodic lattice. QED.",
            styles,
        ),
        equation("gap=(&mu;/3)[1-cos(2&pi;/n)]=(2&mu;/3)sin<sup>2</sup>(&pi;/n)", styles),
        body(
            "The exact finite-grid minimum is &lambda;<sub>min</sub>=1-2&mu; for even n and &lambda;<sub>min</sub>=1-&mu;[1+cos(&pi;/n)] for odd n. Hence all multipliers are nonnegative exactly when &mu;&le;1/2 on an even grid and &mu;&le;1/[1+cos(&pi;/n)] on an odd grid. The FPM viscosity domain 0.50&le;&Omega;<sub>0</sub>&le;0.85, equivalently 0.15&le;&mu;&le;0.50, is a grid-independent sufficient condition. In that domain every nonconstant Fourier mode is damped without sign alternation.",
            styles,
        ),
        body(
            "For zero-mean f, ||P<sup>t</sup>f||<sub>2</sub>&le;&rho;<sup>t</sup>||f||<sub>2</sub>, where &rho;=max<sub>k&ne;0</sub>|&lambda;(k)|; in the monotone FPM domain &rho;=&lambda;<sub>1</sub>=1-gap. For a point-mass initial distribution on N=n<sup>3</sup> sites, TV(P<sup>t</sup>&delta;<sub>x</sub>,uniform)&le;sqrt(N-1)&rho;<sup>t</sup>/2. This provides an explicit total-variation mixing-time bound.",
            styles,
        ),
        body(
            "For every nonconstant mode with &lambda;(k)&ne;0, its exact envelope damping rate is &gamma;<sub>k</sub>=-ln|&lambda;(k)|/&Delta;t. A zero multiplier is annihilated in one tick; a negative multiplier has the same envelope rate and alternates sign. In the declared FPM domain all multipliers are nonnegative, so the slowest nonconstant rate is -ln(&rho;)/&Delta;t, the constant-mode rate is zero, and the fastest finite positive-mode rate is -ln(min<sub>&lambda;&gt;0</sub>&lambda;)/&Delta;t.",
            styles,
        ),
        body(
            "Let u be a passively transported scalar, u<sup>t+1</sup>=Pu<sup>t</sup>. At long wavelength, &lambda;(k)=1-(&mu;&Delta;x<sup>2</sup>/6)|k|<sup>2</sup>+(&mu;&Delta;x<sup>4</sup>/72)&Sigma;<sub>a</sub>k<sub>a</sub><sup>4</sup>+O((k&Delta;x)<sup>6</sup>). For a fixed periodic physical torus of side length &ell;, take &Delta;x=&ell;/n and &Delta;t=&mu;&Delta;x<sup>2</sup>/(6D). For each fixed Fourier wavevector k, &lambda;<sub>&Delta;x</sub>(k)<sup>floor(t/&Delta;t)</sup>&rarr;exp(-D|k|<sup>2</sup>t). For spectrally projected periodic H<sup>s</sup> initial data with s&gt;0, Parseval controls the finite set of retained modes and the H<sup>s</sup> tail uniformly; Fourier truncation therefore gives L<sup>2</sup> convergence of the frozen transport semigroup to &part;<sub>t</sub>u=D&nabla;<sup>2</sup>u on every bounded time interval. The selected A5 length/time values instead give a fixed-scale coefficient D=&mu;&Delta;x<sup>2</sup>/(6&Delta;t); they do not by themselves establish a refinement limit for the runtime route-cost trajectory.",
            styles,
        ),
        body(
            "The fourth-order term is the leading cubic-grid anisotropy. An exact finite-grid shell comparison uses n=7 and the equal-|m|<sup>2</sup>=9 modes (3,0,0) and (2,2,1); their distinct fourth moments split their exact multipliers. The corresponding power ratio after t ticks is [&lambda;<sub>300</sub>/&lambda;<sub>221</sub>]<sup>2t</sup>. This is an exact shell splitting, rather than a comparison of directions unavailable on the same finite torus.",
            styles,
        ),
        statement(
            "Scope boundary",
            "This diagonal Fourier result and its continuum statement apply to a repeatedly transported scalar under the frozen homogeneous kernel only. In the full reference runtime, route cost is recalculated from state and the kernel has state-dependent activity and viscosity; it remains local and conservative but is not translation invariant tick by tick.",
            styles,
        ),
    ]

    s += [
        h1("6. Exact closure theorems", styles),
        h2("6.1 Interior update", styles),
        body(
            "Let L<sub>i,t</sub>&ge;0 be the action paid at site i during tick t. The replenishment received at i is the transpose action of the local kernel:",
            styles,
        ),
        equation("r<sub>i,t</sub> = &Sigma;<sub>j</sub>P<sub>ji,t</sub>L<sub>j,t</sub> = (P<sub>t</sub><super>T</super>L<sub>t</sub>)<sub>i</sub>", styles),
        equation("E<sub>i,t+1</sub> = E<sub>i,t</sub> - L<sub>i,t</sub> + r<sub>i,t</sub>", styles),
        statement(
            "Theorem 3 (Global interior conservation)",
            "For the ordinary, unclipped interior update, &Sigma;<sub>i</sub>E<sub>i,t+1</sub>=&Sigma;<sub>i</sub>E<sub>i,t</sub>.",
            styles,
        ),
        body(
            "Proof. Row stochasticity gives &Sigma;<sub>i</sub>r<sub>i,t</sub>=&Sigma;<sub>j</sub>L<sub>j,t</sub>&Sigma;<sub>i</sub>P<sub>ji,t</sub>=&Sigma;<sub>j</sub>L<sub>j,t</sub>. The debit and replenishment sums cancel. QED.",
            styles,
        ),
        h2("6.2 Antisymmetric edge flux", styles),
        equation("J<sub>i&rarr;j,t</sub> = P<sub>ij,t</sub>L<sub>i,t</sub> - P<sub>ji,t</sub>L<sub>j,t</sub>", styles),
        statement(
            "Theorem 4 (Nodewise continuity)",
            "J<sub>i&rarr;j,t</sub>=-J<sub>j&rarr;i,t</sub> and each vertex obeys E<sub>i,t+1</sub>-E<sub>i,t</sub>+&Sigma;<sub>j in N(i)</sub>J<sub>i&rarr;j,t</sub>=0.",
            styles,
        ),
        body(
            "Proof. Antisymmetry follows by exchanging i and j. Summing the outgoing flux gives L<sub>i,t</sub>&Sigma;<sub>j</sub>P<sub>ij,t</sub>-&Sigma;<sub>j</sub>P<sub>ji,t</sub>L<sub>j,t</sub>=L<sub>i,t</sub>-r<sub>i,t</sub>. Substitution into the energy update proves the identity. QED.",
            styles,
        ),
        h2("6.3 Regional balance", styles),
        equation("E<sub>U</sub>(t+1)-E<sub>U</sub>(t) = - &Sigma;<sub>i in U, j outside U</sub>J<sub>i&rarr;j,t</sub>", styles),
        statement(
            "Theorem 5 (Exact regional boundary law)",
            "For every subset U of V, the change of stored interior energy in U equals the negative net flux across its graph boundary.",
            styles,
        ),
        body(
            "Proof. Sum Theorem 4 over i in U. Every internal edge appears twice with opposite orientation and cancels. Only edges with one endpoint in U remain. QED.",
            styles,
        ),
        h2("6.4 Finite propagation cone", styles),
        statement(
            "Theorem 6 (One-edge causal support)",
            "If two states differ only on a set U at tick t, their ordinary replenishment fields can differ at tick t+1 only on U and its nearest-neighbour boundary. After m ticks, the difference is supported within graph distance m of U.",
            styles,
        ),
        body(
            "Proof. P<sub>ij,t</sub>=0 outside edges and self-loops, so one application of P<sub>t</sub><super>T</super> expands support by at most one edge. Induction gives the m-tick statement. Under A5, graph distance m corresponds to physical distance no greater than mc&Delta;t. QED.",
            styles,
        ),
        h2("6.5 Equilibrium recovery of global weighting", styles),
        statement(
            "Theorem 7 (Local-to-mean-field limit)",
            "Fix a connected finite graph, positive weights, and a kernel P with a positive self-loop. For every non-negative packet q, (P<super>T</super>)<sup>m</sup>q converges to (&Sigma;<sub>j</sub>q<sub>j</sub>)&rho;<super>eq</super> as m&rarr;&infin;.",
            styles,
        ),
        body(
            "Proof. Positivity on connected edges makes P irreducible. A positive self-loop makes it aperiodic. The finite Markov chain therefore has the unique stationary distribution &rho;<super>eq</super> established by detailed balance, and its powers converge to the stationary projection. QED.",
            styles,
        ),
        equation("r<sub>i</sub><sup>eq</sup> = (&Sigma;<sub>j</sub>L<sub>j</sub>) w<sub>i</sub>/(&Sigma;<sub>k</sub>w<sub>k</sub>)", styles),
        body(
            "The globally normalized formula is thus retained at its correct level: it is the frozen-weight equilibrium of repeated nearest-neighbour transport. The microscopic law remains local at every tick.",
            styles,
        ),
        h2("6.6 Expanded signed ledger", styles),
        body(
            "Finite capacity introduces branches that stored energy alone cannot represent. Let X<sub>i</sub>(t) be the cumulative exhaust or paid-erasure amount recorded at the site where removal occurs, and let D<sub>i</sub>(t) be the cumulative zero-boundary deficit recorded at the affected site. Define the observer-level audit totals X(t)=&Sigma;<sub>i</sub>X<sub>i</sub>(t) and D(t)=&Sigma;<sub>i</sub>D<sub>i</sub>(t). Then",
            styles,
        ),
        equation("E<sub>closed</sub>(t) = &Sigma;<sub>i</sub>E<sub>i,t</sub> + X(t) - D(t)", styles),
        statement(
            "Theorem 8 (Expanded ledger closure)",
            "If every capacity removal increments X by the same amount and every zero-boundary deficit increments D by the same amount, then E<sub>closed</sub>(t+1)=E<sub>closed</sub>(t). Internal overflow routing changes neither account.",
            styles,
        ),
        body(
            "Proof. The ordinary interior update conserves the stored sum. Removing an amount x from storage changes the sum by -x and X by +x. Raising a negative raw state to zero changes the stored sum by +d and D by +d. Each paired change cancels in E<sub>closed</sub>. Internal transfers cancel pairwise by Theorem 5. QED.",
            styles,
        ),
        body(
            "Updating X<sub>i</sub> or D<sub>i</sub> at the event site does not transmit a signal to another vertex and therefore does not enlarge the causal cone. The global X(t) and D(t) are sums evaluated after the tick for conservation auditing. If exhaust is later represented as a propagating physical field, that field requires its own local state and transport law; Theorem 8 makes no instantaneous propagation claim.",
            styles,
        ),
        statement(
            "Correct conservation statement",
            "Ordinary interior replenishment obeys exact local conservation. When capacity boundaries, starvation, information erasure, or explicit structural operations occur, the expanded signed ledger is the conserved object.",
            styles,
        ),
    ]

    s += [
        h1("7. Finite action and causal order", styles),
        h2("7.1 Finite work capacity", styles),
        statement(
            "Theorem 9 (Finite operation bound)",
            "If a site has available energy E and every executed non-null operation costs at least c<sub>0</sub>&gt;0, then at most floor(E/c<sub>0</sub>) such operations can be executed without replenishment.",
            styles,
        ),
        body(
            "Proof. N operations cost at least Nc<sub>0</sub>. Affordability requires Nc<sub>0</sub>&le;E, hence N&le;E/c<sub>0</sub>. Since N is integral, N&le;floor(E/c<sub>0</sub>). QED.",
            styles,
        ),
        body(
            "This theorem is the exact mathematical content of finite possibility pressure: a finite budget and positive maintenance cost prevent unbounded simultaneous work. A particular consolidation response is then a constitutive dynamics, developed in Paper 3.",
            styles,
        ),
        h2("7.2 Order sensitivity", styles),
        statement(
            "Theorem 10 (Causal order criterion)",
            "Let F and G be two admissible state-update maps. Exchanging their order changes the state exactly when their composition commutator [F,G](X)=F(G(X))-G(F(X)) is non-zero.",
            styles,
        ),
        body(
            "The statement is algebraic but consequential. When an early update changes energy, viscosity, or route weight used by the next update, F and G generally do not commute. Tick order is then observable inside the model rather than a relabelling convention.",
            styles,
        ),
    ]

    s += [
        h1("8. Geometric closure of directed asymmetry", styles),
        body(
            "The site-local antisymmetric matrix A=(R-R<super>T</super>)/2 has three independent components. Antisymmetry alone does not make those components an exact form. A geometric bridge must first assign them to an oriented plaquette 2-cochain on the periodic cubic cell complex K. Let C<sub>k</sub>(K) denote oriented k-chains, let &part; be the chain-boundary operator, and let d be the discrete coboundary defined by (d&phi;)(&sigma;<sup>2</sup>)=&phi;(&part;&sigma;<sup>2</sup>) for every plaquette &sigma;<sup>2</sup> [4]. The exact-cochain sector is the additional structural condition A=d&phi; for a discrete edge 1-cochain &phi;.",
            styles,
        ),
        statement(
            "Theorem 11 (Discrete closed-boundary exact-cochain identity)",
            "If the plaquette field A is the discrete coboundary d&phi;, then for every oriented cubic 3-chain V the cochain-chain pairing of A with the closed boundary &part;V vanishes.",
            styles,
        ),
        equation("A(&part;V) = (d&phi;)(&part;V) = &phi;(&part;<sup>2</sup>V) = 0", styles),
        body(
            "Proof. The defining duality of the discrete coboundary moves d from the cochain to the chain boundary. Every oriented cell complex satisfies &part;<sup>2</sup>=0, so the boundary of the closed boundary is empty. QED. This is the lattice analogue of Stokes' theorem and requires no continuum derivative.",
            styles,
        ),
        body(
            "Exactness is a restriction, not a consequence of the nine-channel ledger. On the periodic three-torus, closed cochains can also contain nontrivial global cohomology sectors; those are not covered by Theorem 11 unless their periods vanish. A smooth interpolation gives the continuum corollary &int;<sub>&part;V</sub>d&phi;=&int;<sub>V</sub>d<sup>2</sup>&phi;=0, but the discrete theorem is primary. Any identification with torque, torsion links, or entanglement additionally requires the bridge map in Paper 5.",
            styles,
        ),
    ]

    s += [
        h1("9. Continuum scaling", styles),
        body(
            "The exact microscopic theory is discrete. A continuum conservation equation can nevertheless arise under a controlled finite-volume limit. Associate each vertex with a cubic cell of volume &Delta;x<sup>3</sup>, define the coarse energy density e<sup>&Delta;</sup>=E/(&Delta;x<sup>3</sup>), and divide the regional balance by &Delta;t.",
            styles,
        ),
        equation("[E<sub>U</sub>(t+1)-E<sub>U</sub>(t)]/&Delta;t = - &Sigma;<sub>i in U,j outside U</sub>J<sub>i&rarr;j,t</sub>/&Delta;t", styles),
        statement(
            "Theorem 12 (Conditional continuum conservation)",
            "If the piecewise-constant energy interpolants and oriented edge-flux interpolants converge weakly as &Delta;x,&Delta;t&rarr;0 with &Delta;x/&Delta;t fixed, and if their discrete divergences are uniformly controlled, then the limit satisfies &part;<sub>t</sub>e+&nabla;&middot;j=0 in the distributional sense.",
            styles,
        ),
        body(
            "Proof sketch. Multiply the nodewise continuity equation by a smooth compactly supported test function, sum over sites and ticks, and apply discrete summation by parts. Internal edge terms pair antisymmetrically. Under the stated convergence and control assumptions, the discrete time difference and graph divergence converge to their distributional counterparts. The limiting weak identity is the conservation law. This is the standard conservative finite-volume mechanism [3].",
            styles,
        ),
        body(
            "The continuum equation is therefore a limit of the local ledger, not a replacement for it. Exact microscopic conservation holds before any smoothness assumption is made.",
            styles,
        ),
    ]

    s += [
        KeepTogether([
            h1("10. Dependency structure", styles),
            body(
                "The modular series is organized so that later claims expose their dependence on the foundation. The following table is the formal hand-off from this paper.",
                styles,
            ),
            table([
                ["Object or result", "Status here", "Primary downstream use"],
                ["Finite periodic cubic substrate", "Axiom A1", "Executable reference and exact-ledger realization"],
                ["Positive bounded route cost", "Axiom A2", "Action floor, consolidation, and lag constructions"],
                ["Expanded signed accounting", "Axiom A3 + Theorem 8", "Starvation, erasure, exhaust, and structural ledgers"],
                ["Ordered one-edge ticks", "Axiom A4 + Theorems 6 and 10", "Carrier evolution and physical propagation map"],
                ["Speed calibration", "Axiom A5", "Physical length and time scales"],
                ["Nine-entry directed route ledger", "Definition + Propositions 1-3", "Carrier channels, mobility, torsion, and bridge sources"],
                ["Mobility and viscosity", "Constitutive C1 + Proposition 4", "Executable dynamics and bridge response"],
                ["Local kernel", "Constitutive C2 + Theorems 1-7", "Exact replenishment, equilibrium, and causality"],
                ["Exact-cochain boundary closure", "Structural restriction + Theorem 11", "Structural-link and torsion bridge"],
            ], [48 * mm, 50 * mm, 56 * mm], styles),
        ]),
        h2("10.1 Results that do not depend on physical calibration", styles),
        bullet("Kernel stochasticity and detailed balance", styles),
        bullet("Global, nodewise, and regional conservation", styles),
        bullet("Finite graph propagation cone", styles),
        bullet("Equilibrium recovery of activity-weighted replenishment", styles),
        bullet("Finite operation bound", styles),
        bullet("Exact-cochain closed-boundary identity, conditional on A=d&phi;", styles),
        h2("10.2 Results that use A5", styles),
        body(
            "A5 is required only when graph distance and tick count are expressed in metres and seconds. It does not participate in the algebraic closure proofs. This clean separation allows the mathematical core to be tested independently of any proposed physical scale.",
            styles,
        ),
    ]

    s += [
        h1("11. Conclusion", styles),
        body(
            "FPM's foundation is a finite, causal, locally conservative mechanics. The route ledger retains directional information that scalar models discard. The Metropolis-type transport law turns local viscosity and activity into an exactly reversible nearest-neighbour kernel. Its transpose redistributes paid action without creating an all-to-all channel, and its antisymmetric flux gives an exact continuity equation on every node and every region. Repeated transport recovers the global activity-weighted distribution only at equilibrium, resolving the distinction between local dynamics and mean-field closure.",
            styles,
        ),
        body(
            "The framework therefore begins with a complete mathematical substrate: finite state, positive action cost, ordered local propagation, and signed closure. The next paper instantiates these objects in the public reference simulator and audits the numerical realization against every theorem proved here.",
            styles,
        ),
        statement(
            "Foundational summary",
            "Finite resources do more than limit a calculation. Once alternatives are stored in directed local state and every update pays a positive cost, finiteness produces a causal transport geometry with exact local accounting.",
            styles,
        ),
    ]

    s += [
        PageBreak(),
        h1("References", styles),
        reference("[1] N. Metropolis, A. W. Rosenbluth, M. N. Rosenbluth, A. H. Teller, and E. Teller, “Equation of State Calculations by Fast Computing Machines,” <i>Journal of Chemical Physics</i> 21, 1087–1092 (1953). <a href='https://doi.org/10.1063/1.1699114'>https://doi.org/10.1063/1.1699114</a>", styles),
        reference("[2] W. K. Hastings, “Monte Carlo Sampling Methods Using Markov Chains and Their Applications,” <i>Biometrika</i> 57, 97–109 (1970). <a href='https://doi.org/10.1093/biomet/57.1.97'>https://doi.org/10.1093/biomet/57.1.97</a>", styles),
        reference("[3] T. Barth, R. Herbin, and M. Ohlberger, “Finite Volume Methods: Foundation and Analysis,” in <i>Encyclopedia of Computational Mechanics, Second Edition</i> (2017). <a href='https://doi.org/10.1002/9781119176817.ecm2010'>https://doi.org/10.1002/9781119176817.ecm2010</a>", styles),
        reference("[4] M. Desbrun, E. Kanso, and Y. Tong, “Discrete Differential Forms for Computational Modeling,” <i>ACM SIGGRAPH 2006 Courses</i> (2006). <a href='https://doi.org/10.1145/1185657.1185665'>https://doi.org/10.1145/1185657.1185665</a>", styles),
        reference("[5] A. Spiker, <i>Finite Possibility Mechanics: A Unified Information-Theoretic Framework</i>, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21352386'>https://doi.org/10.5281/zenodo.21352386</a>", styles),
        reference("[6] A. Spiker, <i>Finite-Possibility-Mechanics-Complete</i>, reproducible source repository. <a href='https://github.com/alxspiker/Finite-Possibility-Mechanics-Complete'>https://github.com/alxspiker/Finite-Possibility-Mechanics-Complete</a>", styles),
        reference("[7] A. Spiker, <i>FPM Reference Python Simulator and Audit Results</i>, Zenodo (2026). <a href='https://doi.org/10.5281/zenodo.21420735'>https://doi.org/10.5281/zenodo.21420735</a>", styles),
    ]
    return s


if __name__ == "__main__":
    print(build_manuscript(SPEC, manuscript))
