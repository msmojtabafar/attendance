# ⏰ Attendance Manager

> A modern desktop attendance management application built with **Python** and **PySide6**.

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![Docker](https://img.shields.io/badge/Docker-Supported-2496ED?logo=docker\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Supported-FCC624?logo=linux\&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

* 🇮🇷 Persian (Jalali) date support
* ⏱️ Automatic attendance calculation
* ➕ Automatic overtime calculation
* ➖ Automatic shortage calculation
* 🕖 Flexible working hours (07:00–09:00)
* ✏️ Edit existing records
* 🗑️ Delete records
* 📊 Live attendance summary
* 📄 Export reports to PDF
* 📗 Export reports to Excel
* 💾 SQLite database
* 🖥️ Clean and user-friendly interface

---

## 📂 Project Structure

```text
attendance_app/
├── fonts/
├── models/
├── reports/
├── services/
├── ui/
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

---

## 🚀 Installation

```bash
git clone https://github.com/msmojtabafar/attendance.git

cd attendance

python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

---

# 🐳 Docker

### Pull the latest image

```bash
docker pull ghcr.io/msmojtabafar/attendance:latest
```

### Run with Docker Compose (Recommended)

Allow Docker to access your X11 display:

```bash
xhost +local:docker
```

Start the application:

```bash
docker compose up
```

Stop the application:

```bash
docker compose down
```

---

### Build the Docker image locally

```bash
docker build -t attendance-manager .
```

Run the locally built image:

```bash
docker run --rm attendance-manager
```

---

## 📦 Releases

Prebuilt binaries are available in the **Releases** section.

* Linux Executable
* Source Code (.zip)
* Source Code (.tar.gz)

---

## 🛠 Technologies

* Python
* PySide6
* SQLite
* OpenPyXL
* ReportLab
* PersianTools
* arabic-reshaper
* python-bidi
* Docker

---

## 🤝 Contributing

Contributions, issues and feature requests are welcome.

If you find this project useful, please consider giving it a ⭐ on GitHub.

---