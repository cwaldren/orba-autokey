#!/usr/bin/env python

import winreg
import os 

# Modify if you've installed AutoIt elsewhere.
AUTOIT_PATH = r"C:\Program Files (x86)\AutoIt3\AutoIt3.exe"

REG_PATH = r"SOFTWARE\Mozilla\NativeMessagingHosts\orba_autokey"

JSON = """
{{
  "name": "orba_autokey",
  "description": "Server to pass messages from Firefox to AutoIt.",
  "path": "{path}",
  "type": "stdio",
  "allowed_extensions": [ "orba_autokey@example.org" ]
}}
"""

BATCH = """@echo off
SET "AUTOIT_EXE={autoit}"
call python {py}
"""


base_dir = os.path.dirname(os.path.realpath(__file__))

json_path = os.path.join(base_dir, "app", "orba_autokey.json")
bat_path = os.path.join(base_dir, "app", "orba_autokey.bat").replace("\\", "\\\\")
py_path = os.path.join(base_dir, "app", "orba_autokey.py")

with open("app/orba_autokey.bat", "w+") as bat_file:
    bat_file.write(BATCH.format(py = py_path, autoit = AUTOIT_PATH))

with open("app/orba_autokey.json","w+") as json_file:
    json_file.write(JSON.format(path = bat_path))

def set_reg(name, value):
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE) as registry_key:
            winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
            winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

set_reg("", json_path)
