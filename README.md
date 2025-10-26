# 🗂️ Python File Organizer Automation

A beginner-friendly **Python automation project** that organizes files in a selected directory based on file type (e.g., Documents, Images, Videos, Archives).  
This project helps you learn **file handling, automation, argument parsing, and logging** in Python — a solid first step toward becoming an automation expert.

---

## 🚀 Features
- Automatically sorts files into categorized folders
- Supports a **dry-run mode** (preview actions safely)
- **Logging**: keeps a record of all moved files for easy tracking
- Customizable file type categories
- Cross-platform (Windows/macOS/Linux)

---

## 🧰 Prerequisites
Make sure you have **Python 3.8+** installed.  
You can check by running:
```bash
python --version
```

---

## 📦 Installation
Clone the repository or copy the project folder:
```bash
git clone https://github.com/yourusername/python-file-organizer.git
cd python-file-organizer
```

(Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
```


## 🧠 Usage
Basic example:
```bash
python organize.py "path/to/folder"
```

Dry run (preview actions without moving files):
```bash
python organize.py "path/to/folder" --dry-run
```

## ⚙️ Enhancements
Planned and optional upgrades:
- [ ] Add an **auto-confirmation prompt** after dry run
- [ ] Implement **undo feature** using the log file
- [ ] Add **GUI interface (Tkinter or PyQt)** for non-terminal users
- [ ] Allow **custom category rules** via config file

---

## 🧑‍💻 Author
**Vy Nguyen**  
Engineer & Developer passionate about automation and embedded systems.  
💼 [GitHub Profile](https://github.com/vyhoangquocnguyen)

---

## 🪪 License
This project is open-source under the **MIT License**.
