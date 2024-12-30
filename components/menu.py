from tkinter import ttk
from tkinter import *
from functools import partial
import functions.arquivos_cascade_functions as arquivo
import functions.edicao_cascade_functions as edicao
import functions.ajuda_cascade_functions as ajudaf

class SubMenu:
    def __init__(self, root_menu):
        self.menu = Menu(root_menu, tearoff=False)

    def add_command(self, title, function):
        self.menu.add_command(label=title, command=function)

class MenuBar:

    def __init__(self, root_window):
       self.root = root_window

       self.menu = Menu(root_window, tearoff=False)

    def add_cascade(self, title, submenu):
        self.menu.add_cascade(label=title, menu=submenu)

    def __getattr__(self, name):
        return getattr(self.menu, name)


def setup_arquivos_menu(parent_menu, root, open_file_path, text_area):
    
    arquivos = SubMenu(parent_menu.menu)
    arquivos.add_command("Novo", partial(arquivo.new_file, open_file_path, text_area, root))
    arquivos.add_command("Abrir", partial(arquivo.open_file, open_file_path, text_area, root))
    arquivos.add_command("Salvar", partial(arquivo.save, open_file_path, text_area, root))
    arquivos.add_command("Salvar como", partial(arquivo.save_as, open_file_path, text_area, root))
    arquivos.add_command("Sair", arquivo.sys_exit)

    root.bind("<Control-q>", lambda event: arquivo.sys_exit())
    root.bind("<Control-n>", lambda event: arquivo.new_file(open_file_path, text_area, root))
    root.bind("<Control-s>", lambda event: arquivo.save(open_file_path, text_area, root))
    root.bind("<Control-d>", lambda event: arquivo.save_as(open_file_path, text_area, root))
    root.bind("<Control-o>", lambda event: arquivo.open_file(open_file_path, text_area, root))

    return arquivos

def setup_edicao_menu(parent_menu, root, open_file_path, text_area):
    editar = SubMenu(parent_menu.menu)
    editar.add_command("Copiar", partial(edicao.copiar, text_area))
    editar.add_command("Colar", partial(edicao.colar, text_area))
    editar.add_command("Recortar", partial(edicao.recortar, text_area))

    return editar

def setup_ajuda_menu(parent_menu, root, open_file_path, text_area):
    ajuda = SubMenu(parent_menu.menu)

    ajuda.add_command("Sobre", partial(ajudaf.sobre,root))
    ajuda.add_command("Atalhos de tecla", partial(ajudaf.atalhos,root))

    root.bind("<F1>", lambda event: ajudaf.sobre(root))
    root.bind("<F2>", lambda event: ajudaf.atalhos(root))

    return ajuda


def setup_main_menu(root, open_file_path, text_area):
    menu_bar = MenuBar(root)

    arquivos = setup_arquivos_menu(menu_bar, root, open_file_path, text_area)
    editar = setup_edicao_menu(menu_bar, root, open_file_path, text_area)
    ajuda = setup_ajuda_menu(menu_bar, root, open_file_path, text_area)

    menu_bar.add_cascade("Arquivo", arquivos.menu)
    menu_bar.add_cascade("Editar", editar.menu)
    menu_bar.add_cascade("Ajuda", ajuda.menu)

    return menu_bar

    