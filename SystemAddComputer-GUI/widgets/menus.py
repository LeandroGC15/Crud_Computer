from tkinter import Menu, Label
                                        #Clase App para iniciar el programa
class Toolbar:
    def __init__(self, root, frame):                                           #Inicializando la clase
        self.__root = root                                              #Obteniendo la ventana raiz
        self.frame = frame                                               #Obteniendo los frames
        self.frame.table('person')                                      #Mostrando personas por defecto
        self.menu = Menu()                                              #Creando el menu

        self.file = Menu(self.menu, tearoff=False)                      #Menu archivo
        self.admin = Menu(self.menu, tearoff=False)                      #Menu administrador
        self.persons = Menu(self.admin, tearoff=False)
        self.computers = Menu(self.admin, tearoff=False)
        self.components = Menu(self.admin, tearoff=False)


        self.menu.add_cascade(menu=self.file, label="Archivo")
        self.file.add_cascade(menu=self.admin, label="Administrar")

        self.admin.add_command(label="Personas", command=self.viewPersons)
        self.admin.add_command(label="Computadores", command=self.viewComputers)
        self.admin.add_command(label="Componentes", command=self.viewComponents)

        self.file.add_separator()
        self.file.add_command(label="Salir", command=self.__root.destroy)

        self.__root.config(menu=self.menu)

        self.statusbar = Label(self.__root, text="", bd=1, anchor='w')
        self.statusbar.grid(row=1, column=0, columnspan=2, sticky='we')

    def viewPersons(self):
        self.frame.table('person')
    
    def viewComputers(self):
        self.frame.table('computer')
    
    def viewComponents(self):
        self.frame.table('component')