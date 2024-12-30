from tkinter import *
from tkinter import ttk
import components.menu as component_menu
import components.textarea as textarea
import components.mainframe as mainframe
import util.check_ext_file as check_ext


#Variáveis importantes
open_file_path = [None]

#Configurações da janela raiz
main_window = mainframe.MainWindow()
main_window.add_frame()

text_area = textarea.TextArea(main_window.root)
text_area.pack()

menu_bar = component_menu.setup_main_menu(main_window.root, open_file_path, text_area.text)

#Checagem de arquivo
check_ext.check_external_file(open_file_path, text_area.text, main_window.root)

#Configurações antes da inicialização
main_window.root.config(menu=menu_bar.menu)
main_window.display()



