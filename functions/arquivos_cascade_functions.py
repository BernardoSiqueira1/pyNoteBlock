import sys
import os
from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox


def new_file(open_file_path, text_area, root):
    option = messagebox.askyesno("Criar novo arquivo", "Deseja criar um novo arquivo? Alterações feitas anteriormente não serão salvas.")

    if option:
        text_area.delete("0.0", END)
        open_file_path[0] = None
        root.title("Sem título - Python NoteBlock")
    else:
        None
        

def open_file(open_file_path, text_area, root):
    file = filedialog.askopenfilename(defaultextension=".pynb", filetypes=[("Arquivos pynb", "*.pynb")]) 

    if file:
        open_file = open(file, "r", encoding="utf-8")

        text_area.delete("0.0", END)
        text_area.insert("0.0", open_file.read())

        open_file_path[0] = file

        root.title(f"{open_file.name} - Python NoteBlock")


def save(open_file_path, text_area, root):
    if not open_file_path[0]:
        save_as(open_file_path, text_area, root)
    else:
        file = open(open_file_path[0], "w", encoding="utf-8")
        file.write(text_area.get("0.0", END))


def save_as(open_file_path, text_area, root):
    file = filedialog.asksaveasfilename(defaultextension=".pynb", filetypes=[("Arquivo pynb", "*.pynb")])

    if file:
        save_file = open(file, "w", encoding="utf-8")
        save_file.write(text_area.get("0.0", END))
        root.title(f"{save_file.name} - Python NoteBlock")
        open_file_path[0] = file


def sys_exit():
    exit()