from openpyxl import Workbook


def minutes_to_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    return f"{hours:02}:{minutes:02}"


def export_excel(rows):

    wb = Workbook()
    ws = wb.active

    ws.title = "Attendance"

    ws.append([
        "تاریخ",
        "ورود",
        "خروج",
        "ساعت حضور",
        "اضافه‌کار",
        "کسرکار"
    ])



    
    for r in rows:

        ws.append([
            r["work_date"],
            r["check_in"],
            r["check_out"],
            minutes_to_time(r["work_minutes"]),
            minutes_to_time(r["overtime_minutes"]),
            minutes_to_time(r["shortage_minutes"])
        ])

    wb.save("reports/attendance.xlsx")