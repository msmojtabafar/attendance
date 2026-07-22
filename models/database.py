import sqlite3

DB_NAME = "attendance.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    work_date TEXT,
    day_type TEXT,
    check_in TEXT,
    check_out TEXT,
    work_minutes INTEGER,
    overtime_minutes INTEGER,
    shortage_minutes INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_record(
        work_date,
        day_type,
        check_in,
        check_out,
        work_minutes,
        overtime,
        shortage
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO attendance(
        work_date,
        day_type,
        check_in,
        check_out,
        work_minutes,
        overtime_minutes,
        shortage_minutes
    )
    VALUES(?,?,?,?,?,?,?)
    """, (
        work_date,
        day_type,
        check_in,
        check_out,
        work_minutes,
        overtime,
        shortage
    ))

    conn.commit()
    conn.close()

def get_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM attendance
    ORDER BY work_date
    """)

    rows = cur.fetchall()
    conn.close()
    return rows



def delete_record(record_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM attendance WHERE id=?",
        (record_id,)
    )

    conn.commit()
    conn.close()


def update_record(
        record_id,
        work_date,
        day_type,
        check_in,
        check_out,
        work_minutes,
        overtime,
        shortage
):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE attendance
        SET
            work_date=?,
            day_type=?,
            check_in=?,
            check_out=?,
            work_minutes=?,
            overtime_minutes=?,
            shortage_minutes=?
        WHERE id=?
    """, (
        work_date,
        day_type,
        check_in,
        check_out,
        work_minutes,
        overtime,
        shortage,
        record_id
    ))

    conn.commit()
    conn.close()