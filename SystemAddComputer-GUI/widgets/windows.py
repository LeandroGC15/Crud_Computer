from tkinter import Tk, Frame, Label
from .menus import Toolbar
from .table import Table
from .buttons import *

class App:                              #Clase App para iniciar el programa
    def __init__(self):                                                  #Inicializando la clase
        self.__root = Tk()                                               #Creando la ventana principal
        self.__root.title("System Add Computer")                         #Titulo de la ventana
        self.__root.resizable(False, False)                              #Bloqueando el redimensionamiento de la ventana
        self.__root.grid_rowconfigure(0, weight=1)                       #Aplicando grillas 1 fila 2 columnas
        self.__root.grid_columnconfigure(1, weight=1)
        self._screen_width = self.__root.winfo_screenwidth()             #Obteniendo el ancho y alto de la pantalla
        self._screen_height = self.__root.winfo_screenheight()

        self.x = (self._screen_width // 2) - (720 // 2)                    #Obteniendo el valor de x e y
        self.y = (self._screen_height // 2) - (480 // 2)                   #para centrar la ventana

        self.__root.geometry(f"{720}x{480}+{self.x}+{self.y}")     #Centrando la ventana

        self.__root.iconbitmap("assets/images/icon.ico")                                #Icono de la ventana

        self.frame = Frames(self.__root)                                         #Creando los frames de la ventana en varios lados
        Toolbar(self.__root, self.frame)                                        #Creando la barra de menu

    def Init(self):
        self.__root.mainloop()

class Frames:
    def __init__(self, root):
        self.__root = root
        self.center = Frame(self.__root, border=2, relief='groove', bg='ivory2', width=250, height=190, padx=3, pady=3)
        self.center.grid_rowconfigure(1, weight=2)  
        self.center.grid_columnconfigure(0, weight=2)  
        self.top = Frame(self.center, border=2, relief='groove',bg='cornsilk3', width=250, height=90, padx=3, pady=3)
        self.top.grid_rowconfigure(0, weight=1)  
        self.top.grid_columnconfigure(4, weight=1) 
        self.right = Frame(self.__root, border=2, relief='groove',bg='cornsilk3', width=200, height=190)
        self.top.grid(row=0, column=0, sticky="nwe")
        self.center.grid(row=0, column=1, sticky="nsew")
        self.right.grid(row=0, column=2, sticky="ns")

        Search(self.top)                                                      #Creando un buscado

    def table(self, option):
        match option:
            case 'person':
                Table(self.center, "person", [])
            case 'computer':
                Table(self.center, "computer", [])
            case 'component':
                Table(self.center, "component", [])
