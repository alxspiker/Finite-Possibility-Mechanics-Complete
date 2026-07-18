#!/usr/bin/env python3
"""Generate the one-page FPM modular series DOI and relationship map."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output" / "pdf"
OUTPUT_FILE = OUTPUT_DIR / "00_FPM_Modular_Series_Index.pdf"

PAGE_WIDTH, PAGE_HEIGHT = A4
NAVY = colors.HexColor("#14243E")
NAVY_DARK = colors.HexColor("#081524")
NAVY_MID = colors.HexColor("#294A6D")
GOLD = colors.HexColor("#D4A574")
INK = colors.HexColor("#1E2936")
MUTED = colors.HexColor("#607083")
PALE = colors.HexColor("#EEF2F6")
LINE = colors.HexColor("#C8D3DF")

SERIES_DOI = "10.5281/zenodo.21420798"
MONOLITH_DOI = "10.5281/zenodo.21352386"
SIMULATOR_DOI = "10.5281/zenodo.21420735"
REPOSITORY_URL = "https://github.com/alxspiker/Finite-Possibility-Mechanics-Complete"

PAPERS = [
    ("01", "FPM Foundations", "10.5281/zenodo.21420508", "Finite substrate, route ledger, local transport, and exact closure."),
    ("02", "Executable FPM", "10.5281/zenodo.21420643", "Reference runtime, numerical contract, and reproducible audit."),
    ("03", "Finite Carrier and Information Dynamics", "10.5281/zenodo.21420648", "Coherence, consolidation, information accounting, and finite allocation."),
    ("04", "Tensorless Exact-Ledger Sandbox", "10.5281/zenodo.21420650", "Deterministic integer policies and the boundary with reference FPM."),
    ("05", "Phenomenological Bridges", "10.5281/zenodo.21420652", "Declared correspondences with quantum, gravitational, and cosmological observables."),
    ("06", "Empirical Audit and Falsification", "10.5281/zenodo.21420655", "Evidence levels, reproduction standards, and decisive empirical tests."),
]


def _register_fonts() -> tuple[str, str]:
    candidates = [
        (Path("/System/Library/Fonts/Supplemental/Arial.ttf"), Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")),
        (Path("/Library/Fonts/Arial.ttf"), Path("/Library/Fonts/Arial Bold.ttf")),
    ]
    for regular, bold in candidates:
        if regular.exists() and bold.exists():
            try:
                pdfmetrics.registerFont(TTFont("FPM-Index-Regular", str(regular)))
                pdfmetrics.registerFont(TTFont("FPM-Index-Bold", str(bold)))
                return "FPM-Index-Regular", "FPM-Index-Bold"
            except Exception:
                pass
    return "Helvetica", "Helvetica-Bold"


REGULAR, BOLD = _register_fonts()


def doi_link(doi: str) -> str:
    url = f"https://doi.org/{doi}"
    return f"<link href='{url}' color='#294A6D'>{doi}</link>"


def url_link(url: str, label: str) -> str:
    return f"<link href='{url}' color='#294A6D'>{label}</link>"


def styles() -> dict[str, ParagraphStyle]:
    return {
        "eyebrow": ParagraphStyle(
            "IndexEyebrow", fontName=BOLD, fontSize=8.2, leading=10,
            textColor=GOLD, alignment=TA_CENTER, spaceAfter=2.3 * mm,
        ),
        "title": ParagraphStyle(
            "IndexTitle", fontName=BOLD, fontSize=20, leading=23,
            textColor=colors.white, alignment=TA_CENTER, spaceAfter=2.2 * mm,
        ),
        "subtitle": ParagraphStyle(
            "IndexSubtitle", fontName=REGULAR, fontSize=9.6, leading=13,
            textColor=colors.HexColor("#DCE5EE"), alignment=TA_CENTER,
        ),
        "heading": ParagraphStyle(
            "IndexHeading", fontName=BOLD, fontSize=10.4, leading=13,
            textColor=NAVY, spaceBefore=2.2 * mm, spaceAfter=1.5 * mm,
        ),
        "body": ParagraphStyle(
            "IndexBody", fontName=REGULAR, fontSize=8.15, leading=11.2,
            textColor=INK, alignment=TA_LEFT,
        ),
        "small": ParagraphStyle(
            "IndexSmall", fontName=REGULAR, fontSize=7.35, leading=9.5,
            textColor=MUTED,
        ),
        "record": ParagraphStyle(
            "IndexRecord", fontName=REGULAR, fontSize=7.25, leading=9.2,
            textColor=INK,
        ),
        "record_bold": ParagraphStyle(
            "IndexRecordBold", fontName=BOLD, fontSize=7.4, leading=9.3,
            textColor=NAVY,
        ),
        "record_header": ParagraphStyle(
            "IndexRecordHeader", fontName=BOLD, fontSize=7.4, leading=9.3,
            textColor=colors.white,
        ),
    }


def draw_page(canvas, _doc) -> None:
    canvas.saveState()
    header_height = 51 * mm
    steps = 60
    for i in range(steps):
        ratio = i / max(steps - 1, 1)
        red = NAVY_DARK.red + (NAVY_MID.red - NAVY_DARK.red) * ratio
        green = NAVY_DARK.green + (NAVY_MID.green - NAVY_DARK.green) * ratio
        blue = NAVY_DARK.blue + (NAVY_MID.blue - NAVY_DARK.blue) * ratio
        canvas.setFillColorRGB(red, green, blue)
        canvas.rect(0, PAGE_HEIGHT - header_height + i * header_height / steps,
                    PAGE_WIDTH, header_height / steps + 1, fill=1, stroke=0)
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(1)
    canvas.line(18 * mm, PAGE_HEIGHT - 10 * mm, PAGE_WIDTH - 18 * mm, PAGE_HEIGHT - 10 * mm)
    canvas.setFont(REGULAR, 6.8)
    canvas.setFillColor(MUTED)
    canvas.drawString(18 * mm, 8.5 * mm, "FINITE POSSIBILITY MECHANICS - MODULAR SERIES INDEX")
    canvas.drawRightString(PAGE_WIDTH - 18 * mm, 8.5 * mm, "Alx Spiker - July 2026")
    canvas.restoreState()


def build() -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    st = styles()
    doc = BaseDocTemplate(
        str(OUTPUT_FILE), pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=12 * mm, bottomMargin=13 * mm,
        title="Finite Possibility Mechanics Modular Series: DOI and Relationship Map",
        author="Alx Spiker",
        subject="Canonical index for the FPM modular papers and reference simulator",
        keywords="Finite Possibility Mechanics, FPM, DOI map, modular research series",
    )
    frame = Frame(
        doc.leftMargin, doc.bottomMargin,
        PAGE_WIDTH - doc.leftMargin - doc.rightMargin,
        PAGE_HEIGHT - doc.topMargin - doc.bottomMargin,
        leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0,
    )
    doc.addPageTemplates([PageTemplate(id="index", frames=[frame], onPage=draw_page)])

    story = [
        Paragraph("FINITE POSSIBILITY MECHANICS", st["eyebrow"]),
        Paragraph("Modular Series DOI and Relationship Map", st["title"]),
        Paragraph(
            f"Canonical series index - <link href='https://doi.org/{SERIES_DOI}' color='#D4A574'>{SERIES_DOI}</link>",
            st["subtitle"],
        ),
        Spacer(1, 17 * mm),
        Paragraph("Abstract", st["heading"]),
        Paragraph(
            "Finite Possibility Mechanics (FPM) is a finite-resource mechanics of directed alternatives, formulated on a finite periodic "
            "cubic lattice. Each site carries bounded energy, a directed 3x3 route-cost ledger, a normalized nine-channel complex carrier, "
            "and local auxiliary state. Ordinary per-tick action is redistributed through a nearest-neighbour reversible Markov kernel and "
            "recorded in a signed ledger, yielding exact finite-graph results for local and global conservation, nodewise and regional "
            "continuity, finite propagation, equilibrium transport, and finite work capacity. The modular series separates this programme "
            "into six independently citable layers: foundations; executable reference semantics; carrier and information dynamics; a "
            "deterministic exact-integer sandbox; phenomenological bridges to quantum, thermodynamic, gravitational, cosmological, and "
            "electromagnetic observables; and an empirical audit and falsification protocol. A public Python simulator and machine-readable "
            "output reproduce the computational checks associated with Papers 01, 02, and 04. The formal and computational results establish "
            "properties of the stated model; bridge correspondences, calibrations, and retrospective comparisons are hypotheses and audits "
            "rather than independent evidence of physical validity. The series therefore presents both a reproducible construction and "
            "explicit empirical failure conditions.",
            st["body"],
        ),
        Paragraph("DOI map", st["heading"]),
    ]

    rows = [[
        Paragraph("Record", st["record_header"]),
        Paragraph("Scope and persistent identifier", st["record_header"]),
    ]]
    for number, title, doi, description in PAPERS:
        rows.append([
            Paragraph(f"PAPER {number}", st["record_bold"]),
            Paragraph(f"<b>{title}</b> - {description}<br/>{doi_link(doi)}", st["record"]),
        ])
    rows.append([
        Paragraph("SIMULATOR", st["record_bold"]),
        Paragraph(
            "<b>FPM Reference Python Simulator and Audit Results</b> - public source and machine-readable audit output; "
            f"supplements Papers 01, 02, and 04 only.<br/>{doi_link(SIMULATOR_DOI)}",
            st["record"],
        ),
    ])
    table = Table(rows, colWidths=[25 * mm, 149 * mm], repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("BACKGROUND", (0, 1), (-1, -1), colors.white),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE]),
        ("LEFTPADDING", (0, 0), (-1, -1), 2.2 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2.2 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 1.25 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 1.25 * mm),
    ]))
    story.append(table)

    story.extend([
        Paragraph("Relationship key", st["heading"]),
        Table([
            [Paragraph("<b>Is derived from</b>", st["small"]), Paragraph(
                f"Papers 01-06 and the simulator/result package identify the unified monolith as their source: {doi_link(MONOLITH_DOI)}.", st["small"])],
            [Paragraph("<b>Is part of</b>", st["small"]), Paragraph(
                f"Each modular paper and the simulator/result package belongs to this series index: {doi_link(SERIES_DOI)}.", st["small"])],
            [Paragraph("<b>Supplements</b>", st["small"]), Paragraph(
                f"The simulator/result package {doi_link(SIMULATOR_DOI)} supplements Papers 01, 02, and 04. No simulator relationship is asserted for Papers 03, 05, or 06.", st["small"])],
        ], colWidths=[31 * mm, 143 * mm], style=TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), PALE),
            ("BOX", (0, 0), (-1, -1), 0.5, LINE),
            ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 2.2 * mm),
            ("RIGHTPADDING", (0, 0), (-1, -1), 2.2 * mm),
            ("TOPPADDING", (0, 0), (-1, -1), 1.4 * mm),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1.4 * mm),
        ])),
        Spacer(1, 2.1 * mm),
        Paragraph(
            f"<b>Reproducible source:</b> {url_link(REPOSITORY_URL, REPOSITORY_URL)}",
            st["small"],
        ),
    ])

    doc.build(story)
    return OUTPUT_FILE


if __name__ == "__main__":
    print(build())
