import sys
import os
from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox

import util.iconresolver as icon

IMG_PATH = icon.get_dist_path()

SOBRE_DESCR = '''
    Versão 0.8 (30/12/2024)

    Sobre:
    Cópia mal feita do bloco de notas no python, eu realmente não tinha nada melhor pra fazer da minha vida nesse fim de ano.

    © BernardoSoft™
    2024
'''

AJUDA_DESCR = '''
    Atalhos de tecla

    Arquivos:

    Novo         Ctrl+N
    Abrir        Ctrl+O
    Salvar       Ctrl+S
    Salvar como  Ctrl+D
    Sair         Ctrl+Q

    Editar:

    Copiar       Ctrl+C
    Colar        Ctrl+V
    Recortar     Ctrl+X

    Ajuda:

    Sobre        F1
    Atalhos      F2
'''

def create_janela_sobre(root):
    janela_sobre = Toplevel(root)
    janela_sobre.title("Sobre - Python NoteBlock")
    janela_sobre.geometry("200x200")
    janela_sobre.resizable(width=0, height=0)
    janela_sobre.iconbitmap(IMG_PATH)

    return janela_sobre

def sobre(root):

    j_sobre = create_janela_sobre(root)
    Label(j_sobre, text=SOBRE_DESCR, wraplength=180,justify=CENTER,font=("Calibri", 10, "bold")).pack()
    print(IMG_PATH)



def create_janela_atalhos(root):
    janela_ajuda = Toplevel(root)
    janela_ajuda.title("Sobre - Python NoteBlock")
    janela_ajuda.geometry("200x320")
    janela_ajuda.resizable(width=0, height=0)
    janela_ajuda.iconbitmap(IMG_PATH)
    print(IMG_PATH)

    return janela_ajuda

def atalhos(root):
    j_atalhos = create_janela_atalhos(root)
    Label(j_atalhos, text=AJUDA_DESCR, wraplength=180,justify=CENTER,font=("Calibri", 10, "bold")).pack()
