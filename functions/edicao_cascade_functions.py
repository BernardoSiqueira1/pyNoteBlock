import sys
import os
from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox

#Acho que essa é a modularização mais inútil que já fiz na vida pqpKKKKKKKKKK

def copiar(text_area):
    try:
        selected_text = text_area.selection_get()

        text_area.clipboard_clear()
        text_area.clipboard_append(selected_text)
    except TclError:
        None


def colar(text_area):
    try:
        selected_text = text_area.clipboard_get()

        text_area.insert("insert", selected_text)
    except TclError:
        None


def recortar(text_area):
    try:
        selected_text = text_area.selection_get()

        text_area.clipboard_clear()
        text_area.clipboard_append(selected_text)

        text_area.delete("sel.first", "sel.last")
    except TclError:
        None

