from tkinter import Button, Label, Text
from .table import Table
import re
class Search:
    def __init__(self, root):
        self.__root = root
        self.data = []
        self.label = Label(self.__root, text='Ci/Id: ', width=6, anchor='center')
        self.label.grid(row=0, column=0, sticky="ns")
        self.text = Text(self.__root, height=1, width=20, borderwidth=2, relief='groove')
        self.text.grid(row=0, column=1, sticky="ns", padx=2)
        BtnSearch(self.__root, self.text)
        BtnUpdate(self.__root, self.text)
        BtnDelete(self.__root, self.text)
        

class BtnSearch:
    def __init__(self, root, text):
        self.__root = root
        self.text = text
        self.button = Button(self.__root, text='Buscar', command=self.search)
        self.button.grid(row=0, column=2, sticky="n", padx=2)

    def search(self):
        if len(self.text.get('1.0', 'end')) > 1:
            data = self.text.get('1.0', 'end').replace('\n', '')
            text = ''
            with open('db/persons.txt', 'r') as file:
                text = file.read()
                file.close()
            patron = r'\[.+'+data+'.+\]'
            search = re.findall(patron, text)

            if search and len(data) > 4:
                for i in range(len(search)):
                    person = search[i][1:-1].replace(' ', '').split(',') 
                print(person)
                Table(self.__root, "person", person)
            else:

                text = ''
                with open('db/computers.txt', 'r') as file:
                    text = file.read()
                    file.close()
                patron = r'\[.+'+data+'.+\]'
                search = re.findall(patron, text)

                if search and len(data) > 4:
                    for i in range(len(search)):
                        computer = search[i][1:-1].replace(' ', '').replace('[\'', '').replace('\'', '').replace(']', '').split(',')
            
                else:
                    text = ''
                    with open('db/components.txt', 'r') as file:
                        text = file.read()
                        file.close()
                    patron = r'\[.+'+data+'.+\]'
                    search = re.findall(patron, text)
                    if search and len(data) > 4:
                        for i in range(len(search)):
                            component = search[i][1:-1].replace(' ', '').split(',')                    
                    else:
                        print("NO")                    
        else:
            print("NOPE")
            

class BtnUpdate:
    def __init__(self, root, text,):
        self.__root = root
        self.text = text
        self.button = Button(self.__root, text='Actualizar', command=self.search)
        self.button.grid(row=0, column=3, sticky="w", padx=10)

    def search(self):
        if len(self.text.get('1.0', 'end')) > 1:
            print(self.text.get('1.0', 'end'))
        else:
            print('No hay nada')

class BtnDelete:
    def __init__(self, root, text,):
        self.__root = root
        self.text = text
        self.button = Button(self.__root, text='Eliminar', command=self.search)
        self.button.grid(row=0, column=4, sticky="w", padx=5)

    def search(self):
        if len(self.text.get('1.0', 'end')) > 1:
            print(self.text.get('1.0', 'end'))
        else:
            print('No hay nada')