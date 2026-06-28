from reportlab.platypus import (
    SimpleDocTemplate,
    Table
)


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
import arabic_reshaper
from bidi.algorithm import get_display
from reportlab.platypus import TableStyle
from reportlab.lib import colors



def minutes_to_time(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return f"{hours:02}:{mins:02}"


def fa(text):
    return get_display(
        arabic_reshaper.reshape(text)
    )


def export_pdf(rows):


    pdfmetrics.registerFont(
    TTFont("Vazir", "fonts/Vazir.ttf")
    )

    styles = getSampleStyleSheet()
    style = styles["Normal"]
    style.fontName = "Vazir"
    style.fontSize = 11



    data = [[
        fa("تاریخ"),
        fa("ورود"),
        fa("خروج"),
        fa("ساعت حضور"),
        fa("اضافه کار"),
        fa("کسر کار")
    ]]

    for r in rows:
        data.append([
            fa(str(r["work_date"])),
            str(r["check_in"]),
            str(r["check_out"]),
            minutes_to_time(r["work_minutes"]),
            minutes_to_time(r["overtime_minutes"]),
            minutes_to_time(r["shortage_minutes"])
        ])

    doc = SimpleDocTemplate(
        "reports/attendance.pdf"
    )

    table = Table(data)


    table.setStyle(TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Vazir"),
        ("FONTSIZE", (0, 0), (-1, -1), 11),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))


    doc.build([table])