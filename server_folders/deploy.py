# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

VER = '1.0'
TOOL_NAME = 'Server_Folders_{}'.format(VER)
PATH = os.path.dirname(os.path.abspath(__file__))
MAIN_FILE = 'server_folders.py'
#ICON = os.path.join('icon', 'FFR.ico')
PYTHON_PATH = r'C:\Users\claudio\AppData\Local\Programs\Python\Python39-32\Lib\site-packages'

with open(MAIN_FILE, 'r') as f:
    data = f.read()

with open(MAIN_FILE, 'w') as f:
    f.write(data.replace('{VERSION}', VER))

# Gerar EXE
#subprocess.call(['pyinstaller', '--path', PYTHON_PATH,'--hidden-import', 'win32timezone', '--icon', ICON, '--onefile', os.path.join(MAIN_FILE)])
subprocess.call(['pyinstaller', '--path', PYTHON_PATH,'--hidden-import', 'win32timezone', '--onefile', '--windowed', os.path.join(MAIN_FILE)])

with open(os.path.join(MAIN_FILE), 'w') as f:
    f.write(data.replace(VER, '{VERSION}'))

#shutil.copy2(os.path.join(PATH, 'Release_Notes.txt'), os.path.join(PATH, 'dist', 'Release_Notes.txt'))
#shutil.copy2(os.path.join(PATH, 'logging.yaml'), os.path.join(PATH, 'dist', 'logging.yaml'))
#shutil.copy2(os.path.join(PATH, 'login.txt'), os.path.join(PATH, 'dist', 'login.txt'))
#shutil.copytree(os.path.join(PATH, 'Icon'), os.path.join(PATH, 'dist', 'Icon'))

# Removing unecessary folders and files
os.remove(os.path.join(PATH, MAIN_FILE.replace('py', 'spec')))
shutil.rmtree(os.path.join(PATH, 'build'))

# Renaming exe folder
os.rename(os.path.join(PATH, 'dist'), os.path.join(PATH, TOOL_NAME))
os.rename(os.path.join(PATH, TOOL_NAME, 'server_folders.exe'), os.path.join(PATH, TOOL_NAME, '{}.exe'.format(TOOL_NAME)))