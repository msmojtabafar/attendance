from datetime import datetime

FMT = "%H:%M"


def to_minutes(t):
    dt = datetime.strptime(t, FMT)
    return dt.hour * 60 + dt.minute


def calculate(check_in, check_out):

    start = to_minutes(check_in)
    end = to_minutes(check_out)

    work = max(end - start, 0)

    if start <= 9 * 60:
        expected_end = start + 480
    else:
        expected_end = 17 * 60

    overtime = max(end - expected_end, 0)

    shortage = max(480 - work, 0)

    if start > 9 * 60:
        shortage += start - (9 * 60)

    return {
        "work": work,
        "overtime": overtime,
        "shortage": shortage
    }