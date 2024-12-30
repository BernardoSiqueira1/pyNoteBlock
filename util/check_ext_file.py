import sys
import os
from tkinter import *

#Checagem pra arquivos .pynb abertos externamente (sem o Open da aplicação)

def open_by_external_file(open_file_path, path, text_area, root):
    file = open(path, "r", encoding="utf-8")
    text_area.insert("0.0", file.read())
    open_file_path[0] = path
    root.title(f"{path} - Python NoteBlock")

def check_external_file(open_file_path, text_area, root):

    try:
        if sys.argv[1]:
            file_path = sys.argv[1]
            open_by_external_file(open_file_path, file_path, text_area, root)
        else:
            None

    except IndexError:
        None
