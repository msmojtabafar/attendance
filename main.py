import sys
import os

from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from models.database import init_db


if __name__ == "__main__":
    os.makedirs("reports", exist_ok=True)
    init_db()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())