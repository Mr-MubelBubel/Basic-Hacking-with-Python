#!/usr/bin/python3

import sqlite3, sys, os

if sys.platform == "win32" or sys.platform == "cygwin":
    path = os.path.join(os.getenv("HOME"), "AppData\\Roaming\\Mozilla\\Firefox")

elif sys.platform == "darwin":
    path = os.path.join(os.getenv("HOME"), "Library/Application Support/Firefox")

else:
    path = os.path.join(os.getenv("HOME"), "firefox")

# Find right folder
subfolders = os.listdir(path)
for subfolder in subfolders:
    cookies_file = os.path.join(os.path.join(path, subfolder), "cookies.sqlite")

    if os.path.isfile(cookies_file):
        break

# Print Cookies Out
conn = sqlite3.connect(cookies_file)
c = conn.cursor()

c.execute("SELECT * FROM moz_cookies")
for result in c.fetchall():
    print(result)

conn.close()