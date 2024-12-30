from tkinter import ttk
from tkinter import *
import util.iconresolver as icon

IMG_PATH = icon.get_dist_path()

class MainWindow():
    def __init__(self):
        self.root = Tk()
        self.root.title("Python NotePad")
        self.root.geometry("400x600")
        self.root.resizable(width=0, height=0)   
        self.root.iconbitmap(IMG_PATH)

    def add_frame(self):
        ttk.Frame(self.root).pack()

    def display(self):
        self.root.mainloop()