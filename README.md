# ⏰ Attendance Manager

> A modern desktop attendance management application built with
> **Python** and **PySide6**.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-MIT-yellow)

------------------------------------------------------------------------

## ✨ Features

-   🇮🇷 Persian (Jalali) date support
-   ⏱️ Automatic attendance calculation
-   ➕ Automatic overtime calculation
-   ➖ Automatic shortage calculation
-   🕖 Flexible working hours (07:00--09:00)
-   ✏️ Edit existing records
-   🗑️ Delete records
-   📊 Live totals (Attendance, Overtime, Shortage)
-   📄 Export reports to **PDF**
-   📗 Export reports to **Excel**
-   💾 SQLite database
-   🖥️ Clean and easy-to-use interface

------------------------------------------------------------------------

## 📂 Project Structure

``` text
attendance_app/
├── fonts/
├── models/
├── reports/
├── services/
├── ui/
├── main.py
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

## 🚀 Installation

``` bash
git clone https://github.com/YOUR_USERNAME/attendance-manager.git
cd attendance-manager

python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

------------------------------------------------------------------------

## 🐳 Docker

Build the image:

``` bash
docker build -t attendance-manager .
```

Run the application:

``` bash
docker run --rm attendance-manager
```

------------------------------------------------------------------------

## 📦 Technologies

-   Python
-   PySide6
-   SQLite
-   OpenPyXL
-   ReportLab
-   PersianTools
-   arabic-reshaper
-   python-bidi

------------------------------------------------------------------------

## 🤝 Contributing

Contributions, issues and feature requests are welcome.

If you like this project, consider giving it a ⭐ on GitHub.

------------------------------------------------------------------------

## 📄 License

Released under the **MIT License**.
