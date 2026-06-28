from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QDateEdit,
    QTimeEdit,
    QTableWidget,
    QTableWidgetItem,
    QLineEdit,
    QMessageBox
)

from functools import partial
from PySide6.QtCore import QTime, QDate

from services.calculator import calculate
from models.database import (
    insert_record,
    get_all,
    delete_record,
    update_record
)

from services.excel_export import export_excel
from services.pdf_export import export_pdf

from persiantools.jdatetime import JalaliDate
from datetime import date


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.editing_id = None
        self.setWindowTitle("Attendance")
        self.resize(900, 600)

        layout = QVBoxLayout()

        row = QHBoxLayout()

        self.date = QDateEdit()
        self.date.setDisplayFormat("yyyy/MM/dd")

        today = JalaliDate.today()

        self.date = QLineEdit()
        self.date.setText(
            f"{today.year:04d}/{today.month:02d}/{today.day:02d}"
        )


        self.in_time = QTimeEdit()
        self.out_time = QTimeEdit()

        self.in_time.setTime(QTime(8, 0))
        self.out_time.setTime(QTime(16, 0))

        row.addWidget(QLabel("Date"))
        row.addWidget(self.date)

        row.addWidget(QLabel("In"))
        row.addWidget(self.in_time)

        row.addWidget(QLabel("Out"))
        row.addWidget(self.out_time)

        save_btn = QPushButton("Save")
        save_btn.clicked.connect(self.save)

        excel_btn = QPushButton("Excel")
        excel_btn.clicked.connect(self.export_excel)

        pdf_btn = QPushButton("PDF")
        pdf_btn.clicked.connect(self.export_pdf)

        row.addWidget(save_btn)
        row.addWidget(excel_btn)
        row.addWidget(pdf_btn)

        layout.addLayout(row)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "تاریخ",
            "ورود",
            "خروج",
            "ساعت حضور",
            "اضافه‌کار",
            "کسرکار",
            "ویرایش",
            "حذف"
        ])

        layout.addWidget(self.table)

        self.setLayout(layout)


        summary_layout = QHBoxLayout()

        self.work_total = QLabel("جمع حضور: 00:00")
        self.ot_total = QLabel("جمع اضافه‌کار: 00:00")
        self.short_total = QLabel("جمع کسرکار: 00:00")

        summary_layout.addWidget(self.work_total)
        summary_layout.addWidget(self.ot_total)
        summary_layout.addWidget(self.short_total)

        layout.addLayout(summary_layout)


        self.load_table()

        self.update_summary()


    def save(self):

        try:

            date = self.date.text().strip()

            check_in = self.in_time.time().toString("HH:mm")
            check_out = self.out_time.time().toString("HH:mm")

            result = calculate(
                check_in,
                check_out
            )

            if self.editing_id is None:

                insert_record(
                    date,
                    check_in,
                    check_out,
                    result["work"],
                    result["overtime"],
                    result["shortage"]
                )

                QMessageBox.information(
                    self,
                    "موفق",
                    "رکورد با موفقیت ذخیره شد."
                )

            else:

                update_record(
                    self.editing_id,
                    date,
                    check_in,
                    check_out,
                    result["work"],
                    result["overtime"],
                    result["shortage"]
                )

                self.editing_id = None

                QMessageBox.information(
                    self,
                    "موفق",
                    "رکورد با موفقیت ویرایش شد."
                )

            self.load_table()

        except Exception as e:

            QMessageBox.critical(
                self,
                "خطا",
                str(e)
            )


    def load_table(self):

        rows = get_all()

        self.table.setRowCount(len(rows))

        for r, row in enumerate(rows):

            self.table.setItem(
                r,
                0,
                QTableWidgetItem(row["work_date"])
            )

            self.table.setItem(
                r,
                1,
                QTableWidgetItem(row["check_in"])
            )

            self.table.setItem(
                r,
                2,
                QTableWidgetItem(row["check_out"])
            )

            self.table.setItem(
                r,
                3,
                QTableWidgetItem(
                    self.minutes_to_time(row["work_minutes"])
                )
            )

            self.table.setItem(
                r,
                4,
                QTableWidgetItem(
                    self.minutes_to_time(row["overtime_minutes"])
                )
            )

            self.table.setItem(
                r,
                5,
                QTableWidgetItem(
                    self.minutes_to_time(row["shortage_minutes"])
                )
            )

            edit_btn = QPushButton("ویرایش")
            delete_btn = QPushButton("حذف")

            edit_btn.clicked.connect(
                partial(
                    self.edit_record,
                    row["id"]
                )
            )

            delete_btn.clicked.connect(
                partial(
                    self.delete_record,
                    row["id"]
                )
            )

            self.table.setCellWidget(
                r,
                6,
                edit_btn
            )

            self.table.setCellWidget(
                r,
                7,
                delete_btn
            )

        self.update_summary()


    def export_excel(self):

        try:

            export_excel(get_all())

            QMessageBox.information(
                self,
                "موفق",
                "فایل Excel با موفقیت ایجاد شد."
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "خطا",
                str(e)
            )


    def export_pdf(self):

        try:

            export_pdf(get_all())

            QMessageBox.information(
                self,
                "موفق",
                "فایل PDF با موفقیت ایجاد شد."
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "خطا",
                str(e)
            )


    def delete_record(self, record_id):

        answer = QMessageBox.question(
            self,
            "حذف",
            "آیا از حذف این رکورد مطمئن هستید؟",
            QMessageBox.Yes | QMessageBox.No
        )

        if answer == QMessageBox.Yes:

            try:

                delete_record(record_id)

                self.load_table()

                QMessageBox.information(
                    self,
                    "موفق",
                    "رکورد با موفقیت حذف شد."
                )

            except Exception as e:

                QMessageBox.critical(
                    self,
                    "خطا",
                    str(e)
                )    


    def edit_record(self, record_id):

        row = get_all()

        record = next(
            x for x in row
            if x["id"] == record_id
        )

        self.date.setText(
            record["work_date"]
        )

        self.in_time.setTime(
            QTime.fromString(
                record["check_in"],
                "HH:mm"
            )
        )

        self.out_time.setTime(
            QTime.fromString(
                record["check_out"],
                "HH:mm"
            )
        )

        self.editing_id = record_id        


    def minutes_to_time(self, minutes):
        h = minutes // 60
        m = minutes % 60
        return f"{h:02}:{m:02}"


    def update_summary(self):

        rows = get_all()

        work = sum(r["work_minutes"] for r in rows)
        overtime = sum(r["overtime_minutes"] for r in rows)
        shortage = sum(r["shortage_minutes"] for r in rows)

        self.work_total.setText(
            f"جمع حضور: {self.minutes_to_time(work)}"
        )

        self.ot_total.setText(
            f"جمع اضافه‌کار: {self.minutes_to_time(overtime)}"
        )

        self.short_total.setText(
            f"جمع کسرکار: {self.minutes_to_time(shortage)}"
        )


