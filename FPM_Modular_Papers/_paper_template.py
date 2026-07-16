#!/usr/bin/env python3
"""Shared visual template for the FPM modular paper series."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Sequence

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    NextPageTemplate,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = ROOT / "output" / "pdf"
PAGE_WIDTH, PAGE_HEIGHT = A4

NAVY = colors.HexColor("#14243E")
NAVY_DARK = colors.HexColor("#081524")
NAVY_MID = colors.HexColor("#294A6D")
GOLD = colors.HexColor("#D4A574")
INK = colors.HexColor("#1E2936")
MUTED = colors.HexColor("#607083")
PALE = colors.HexColor("#EEF2F6")
WHITE = colors.white


@dataclass(frozen=True)
class PaperSpec:
    number: int
    title: str
    subtitle: str
    filename: str
    scope: str
    claim_boundary: str
    sections: Sequence[tuple[str, str]]
    document_label: str = "RESEARCH PAPER"


def _register_fonts() -> tuple[str, str, str]:
    candidates = [
        Path(__file__).resolve().parents[1] / "fonts",
        Path("/System/Library/Fonts/Supplemental"),
        Path("/Library/Fonts"),
    ]
    combinations = [
        ("Avenir Next.ttc", "Avenir Next.ttc", "Avenir Next.ttc"),
        ("Arial.ttf", "Arial Bold.ttf", "Arial Italic.ttf"),
        ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf"),
    ]
    for directory in candidates:
        for regular, bold, italic in combinations:
            paths = [directory / regular, directory / bold, directory / italic]
            if all(path.exists() and path.suffix.lower() == ".ttf" for path in paths):
                try:
                    pdfmetrics.registerFont(TTFont("FPM-Regular", str(paths[0])))
                    pdfmetrics.registerFont(TTFont("FPM-Bold", str(paths[1])))
                    pdfmetrics.registerFont(TTFont("FPM-Italic", str(paths[2])))
                    return "FPM-Regular", "FPM-Bold", "FPM-Italic"
                except Exception:
                    continue
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"


REGULAR, BOLD, ITALIC = _register_fonts()


def _styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(
        name="CoverSeries", fontName=BOLD, fontSize=12, leading=15,
        textColor=GOLD, alignment=TA_CENTER, spaceAfter=11 * mm,
    ))
    styles.add(ParagraphStyle(
        name="CoverTitle", fontName=BOLD, fontSize=29, leading=34,
        textColor=WHITE, alignment=TA_CENTER, spaceAfter=7 * mm,
    ))
    styles.add(ParagraphStyle(
        name="CoverSubtitle", fontName=REGULAR, fontSize=13, leading=19,
        textColor=colors.HexColor("#DCE5EE"), alignment=TA_CENTER,
        spaceAfter=12 * mm,
    ))
    styles.add(ParagraphStyle(
        name="CoverMeta", fontName=REGULAR, fontSize=9.5, leading=15,
        textColor=colors.HexColor("#DCE5EE"), alignment=TA_CENTER,
    ))
    styles.add(ParagraphStyle(
        name="DocTitle", fontName=BOLD, fontSize=24, leading=29,
        textColor=NAVY, spaceAfter=5 * mm,
    ))
    styles.add(ParagraphStyle(
        name="Deck", fontName=REGULAR, fontSize=11.5, leading=17,
        textColor=MUTED, spaceAfter=7 * mm,
    ))
    styles.add(ParagraphStyle(
        name="Heading", fontName=BOLD, fontSize=15, leading=19,
        textColor=NAVY, spaceBefore=5 * mm, spaceAfter=2.5 * mm,
    ))
    styles.add(ParagraphStyle(
        name="BodyFPM", fontName=REGULAR, fontSize=10.2, leading=15.2,
        textColor=INK, spaceAfter=3.5 * mm,
    ))
    styles.add(ParagraphStyle(
        name="Small", fontName=REGULAR, fontSize=8.8, leading=13,
        textColor=MUTED,
    ))
    styles.add(ParagraphStyle(
        name="Callout", fontName=REGULAR, fontSize=10, leading=15,
        textColor=INK,
    ))
    styles.add(ParagraphStyle(
        name="SectionNumber", fontName=BOLD, fontSize=9, leading=12,
        textColor=GOLD,
    ))
    styles.add(ParagraphStyle(
        name="ManuscriptH1", fontName=BOLD, fontSize=17, leading=21,
        textColor=NAVY, spaceBefore=7 * mm, spaceAfter=3 * mm,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="ManuscriptH2", fontName=BOLD, fontSize=12.5, leading=16,
        textColor=NAVY, spaceBefore=5 * mm, spaceAfter=2 * mm,
        keepWithNext=True,
    ))
    styles.add(ParagraphStyle(
        name="Equation", fontName=REGULAR, fontSize=10.3, leading=15,
        textColor=INK, alignment=TA_CENTER, leftIndent=6 * mm,
        rightIndent=6 * mm, spaceBefore=2.5 * mm, spaceAfter=3.5 * mm,
    ))
    styles.add(ParagraphStyle(
        name="DefinitionFPM", fontName=REGULAR, fontSize=10, leading=15,
        textColor=INK,
    ))
    styles.add(ParagraphStyle(
        name="Reference", fontName=REGULAR, fontSize=8.8, leading=12.5,
        textColor=INK, leftIndent=6 * mm, firstLineIndent=-6 * mm,
        spaceAfter=2.2 * mm,
    ))
    styles.add(ParagraphStyle(
        name="BulletFPM", fontName=REGULAR, fontSize=10.2, leading=15.2,
        textColor=INK, leftIndent=5 * mm, firstLineIndent=-3.2 * mm,
        bulletIndent=0, spaceAfter=2.2 * mm,
    ))
    return styles


class ModularPaperDoc(BaseDocTemplate):
    def __init__(self, filename: Path, spec: PaperSpec):
        self.spec = spec
        super().__init__(
            str(filename), pagesize=A4,
            leftMargin=22 * mm, rightMargin=22 * mm,
            topMargin=25 * mm, bottomMargin=22 * mm,
            title=spec.title, author="Alx Spiker",
            subject="Finite Possibility Mechanics modular paper series",
        )
        cover_frame = Frame(20 * mm, 20 * mm, PAGE_WIDTH - 40 * mm, PAGE_HEIGHT - 40 * mm,
                            id="cover-frame", leftPadding=0, rightPadding=0,
                            topPadding=0, bottomPadding=0)
        body_frame = Frame(self.leftMargin, self.bottomMargin,
                           PAGE_WIDTH - self.leftMargin - self.rightMargin,
                           PAGE_HEIGHT - self.topMargin - self.bottomMargin,
                           id="body-frame", leftPadding=0, rightPadding=0,
                           topPadding=0, bottomPadding=0)
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self._draw_cover),
            PageTemplate(id="body", frames=[body_frame], onPage=self._draw_body_chrome),
        ])

    def afterFlowable(self, flowable):
        if not isinstance(flowable, Paragraph):
            return
        style_name = flowable.style.name
        if style_name == "ManuscriptH1":
            self.notify("TOCEntry", (0, flowable.getPlainText(), self.page - 1))
        elif style_name == "ManuscriptH2":
            self.notify("TOCEntry", (1, flowable.getPlainText(), self.page - 1))

    def _draw_cover(self, canvas, _doc):
        canvas.saveState()
        steps = 100
        for i in range(steps):
            ratio = i / max(steps - 1, 1)
            red = NAVY_DARK.red + (NAVY_MID.red - NAVY_DARK.red) * ratio
            green = NAVY_DARK.green + (NAVY_MID.green - NAVY_DARK.green) * ratio
            blue = NAVY_DARK.blue + (NAVY_MID.blue - NAVY_DARK.blue) * ratio
            canvas.setFillColorRGB(red, green, blue)
            canvas.rect(0, i * PAGE_HEIGHT / steps, PAGE_WIDTH,
                        PAGE_HEIGHT / steps + 1, fill=1, stroke=0)
        # Use a pre-blended colour rather than PDF transparency.  The latter
        # renders inconsistently in some Poppler and Preview versions.
        canvas.setFillColor(colors.HexColor("#21405F"))
        path = canvas.beginPath()
        path.moveTo(0, PAGE_HEIGHT * 0.16)
        path.lineTo(PAGE_WIDTH, PAGE_HEIGHT * 0.47)
        path.lineTo(PAGE_WIDTH, PAGE_HEIGHT * 0.60)
        path.lineTo(0, PAGE_HEIGHT * 0.29)
        path.close()
        canvas.drawPath(path, fill=1, stroke=0)
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(1.2)
        canvas.line(22 * mm, PAGE_HEIGHT - 24 * mm, PAGE_WIDTH - 22 * mm, PAGE_HEIGHT - 24 * mm)
        canvas.line(22 * mm, 24 * mm, PAGE_WIDTH - 22 * mm, 24 * mm)
        canvas.restoreState()

    def _draw_body_chrome(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.HexColor("#C7D0DA"))
        canvas.setLineWidth(0.45)
        canvas.line(doc.leftMargin, PAGE_HEIGHT - 16 * mm, PAGE_WIDTH - doc.rightMargin, PAGE_HEIGHT - 16 * mm)
        canvas.setFont(BOLD, 7.4)
        canvas.setFillColor(NAVY)
        canvas.drawString(doc.leftMargin, PAGE_HEIGHT - 12.5 * mm,
                          f"FINITE POSSIBILITY MECHANICS  ·  MODULAR PAPER {self.spec.number:02d}")
        canvas.setFont(REGULAR, 7.4)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(PAGE_WIDTH - doc.rightMargin, 12.5 * mm, str(doc.page - 1))
        canvas.restoreState()


def _cover_story(spec: PaperSpec, styles):
    published = date.today().strftime("%B %Y")
    return [
        Spacer(1, 29 * mm),
        Paragraph("FINITE POSSIBILITY MECHANICS", styles["CoverSeries"]),
        Paragraph(f"MODULAR PAPER {spec.number:02d}", styles["CoverSeries"]),
        Spacer(1, 5 * mm),
        Paragraph(spec.title, styles["CoverTitle"]),
        Paragraph(spec.subtitle, styles["CoverSubtitle"]),
        Table([[""]], colWidths=[42 * mm], rowHeights=[1.2 * mm],
              style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD),
                                ("ALIGN", (0, 0), (-1, -1), "CENTER")])),
        Spacer(1, 13 * mm),
        Paragraph(spec.document_label, styles["CoverSeries"]),
        Paragraph(
            f"Alx Spiker<br/>{published}<br/>Edmonton, Alberta, Canada<br/><br/>"
            "Part of the FPM modular research series",
            styles["CoverMeta"],
        ),
        NextPageTemplate("body"),
        PageBreak(),
    ]


def _callout(label: str, text: str, styles):
    content = Paragraph(f"<b>{label}</b><br/>{text}", styles["Callout"])
    table = Table([[content]], colWidths=[PAGE_WIDTH - 44 * mm], hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PALE),
        ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor("#C8D3DF")),
        ("LINEBEFORE", (0, 0), (0, -1), 3, GOLD),
        ("LEFTPADDING", (0, 0), (-1, -1), 5 * mm),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5 * mm),
        ("TOPPADDING", (0, 0), (-1, -1), 4 * mm),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4 * mm),
    ]))
    return table


def manuscript_styles():
    """Return the shared stylesheet for full modular manuscripts."""
    return _styles()


def h1(text: str, styles):
    return Paragraph(text, styles["ManuscriptH1"])


def h2(text: str, styles):
    return Paragraph(text, styles["ManuscriptH2"])


def body(text: str, styles):
    return Paragraph(text, styles["BodyFPM"])


def equation(text: str, styles):
    return Paragraph(text, styles["Equation"])


def bullet(text: str, styles):
    return Paragraph(f"&bull;&nbsp; {text}", styles["BulletFPM"])


def statement(label: str, text: str, styles):
    return _callout(label, text, styles)


def reference(text: str, styles):
    return Paragraph(text, styles["Reference"])


def contents_page(spec: PaperSpec, styles):
    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(name="TOC1", fontName=BOLD, fontSize=10.2, leading=15,
                       leftIndent=0, firstLineIndent=0, textColor=NAVY,
                       spaceBefore=1.5 * mm),
        ParagraphStyle(name="TOC2", fontName=REGULAR, fontSize=9, leading=13,
                       leftIndent=7 * mm, firstLineIndent=0, textColor=MUTED),
    ]
    return [
        Paragraph("Contents", styles["DocTitle"]),
        Paragraph(f"Modular Paper {spec.number:02d} in the Finite Possibility Mechanics research series", styles["Deck"]),
        Spacer(1, 3 * mm),
        toc,
        PageBreak(),
    ]


def build_manuscript(spec: PaperSpec, manuscript_story) -> Path:
    """Build a complete modular manuscript with a live table of contents."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    destination = OUTPUT_DIR / spec.filename
    styles = _styles()
    doc = ModularPaperDoc(destination, spec)
    story = _cover_story(spec, styles)
    story.extend(contents_page(spec, styles))
    story.extend(manuscript_story(styles))
    doc.multiBuild(story)
    return destination
