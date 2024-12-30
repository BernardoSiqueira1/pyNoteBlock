from tkinter import ttk
from tkinter import *

class TextArea():
    def __init__(self, root):
        self.text = Text(root, width=400, height=600)

    def pack(self):
        self.text.pack()