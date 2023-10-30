from tkinter import ttk, Scrollbar
import re
#Clase que mostrara los datos en una tabla
class Table:
    def __init__(self, frame, option, data):
        self.frame = frame
        self.option = option
        self.data = data
        self.table = ''
        self.hscroll = Scrollbar(self.frame, orient='horizontal')
        self.createTable()
        
        self.table.grid(row=1, column=0, sticky="nswe")
        self.hscroll.config(command=self.table.xview)
        self.hscroll.grid(row=2, column=0, sticky='swe')

    def createTable(self):
        self.header()
        match self.option:            
            case 'person':                                             
                text = ''
                with open('db/persons.txt', 'r') as file:
                    text = file.read()
                    file.close()
                if self.data:
                    list_persons = self.data
                else:
                    patron = r'\[.+\]'
                    list_persons = re.findall(patron, text)

                for i in range(len(list_persons)):
                    person = list_persons[i][1:-1].replace(' ', '').split(',')   
                    print(person[i])                 
                    if i % 2 == 0:
                        self.table.insert("",'end',values=(person[0],person[1],person[2],person[3],person[4], person[5]), tag="gray1")
                    else:
                        self.table.insert("",'end',values=(person[0],person[1],person[2],person[3],person[4], person[5]), tag="gray2")

            case 'computer':
                text = ''
                with open('db/computers.txt', 'r') as file:
                    text = file.read()
                    file.close()
                patron = r'\[.+\]'
                list_computers = re.findall(patron, text)
                for i in range(len(list_computers)):
                    computer = list_computers[i][1:-1].replace(' ', '').replace('[\'', '').replace('\'', '').replace(']', '').split(',')                   
                    if i % 2 == 0:
                        self.table.insert("",'end',values=(computer[0],computer[1],computer[2],computer[3],computer[4], computer[5], computer[6], computer[7], computer[8], computer[9], computer[10]), tag="gray1")
                    else:
                        self.table.insert("",'end',values=(computer[0],computer[1],computer[2],computer[3],computer[4], computer[5], computer[6], computer[7], computer[8], computer[9], computer[10]), tag="gray2")
                        
            case 'component':
                text = ''
                with open('db/components.txt', 'r') as file:
                    text = file.read()
                    file.close()
                patron = r'\[.+\]'
                list_componets = re.findall(patron, text)
                for i in range(len(list_componets)):
                    component = list_componets[i][1:-1].replace(' ', '').split(',')                    
                    if i % 2 == 0:
                        self.table.insert("",'end',values=(component[0],component[1],component[2],component[3]), tag="gray1")
                    else:
                        self.table.insert("",'end',values=(component[0],component[1],component[2],component[3]),tag="gray2")                
                        
        
        
    
    def header(self):
        match self.option:
            case 'person':                
                self.table = ttk.Treeview(self.frame, columns=('firstname', 'lastname', 'age', 'ci', 'computer', 'computerid'), show="headings", xscrollcommand=self.hscroll.set)
                for col in self.table["columns"]:                                    # Establecer el ancho de las columnas
                    if col != "#0":                                                 # Excluir la columna "#0"
                        self.table.column(col, width=100, anchor="w")
                self.table.heading("firstname", text="Nombre", anchor="w")
                self.table.heading("lastname", text="Apellido", anchor="w")
                self.table.heading("age", text="Edad", anchor="w")
                self.table.heading("ci", text="CI", anchor="w")
                self.table.heading("computer", text="Computadora", anchor="w")
                self.table.heading("computerid", text="ID Computadora", anchor="w")

            case 'computer':                
                self.table = ttk.Treeview(self.frame, columns=('namepc', 'id', 'cpu', 'memory', 'monitor', 'keyboard', 'mouse', 'power', 'diks', 'motherboard', 'person'), show="headings", xscrollcommand=self.hscroll.set)
                for col in self.table["columns"]:                                    
                    if col != "#0":                                                 
                        self.table.column(col, width=80, anchor="w")
                self.table.heading("namepc", text="PC", anchor="w")
                self.table.heading("id", text="ID", anchor="w")
                self.table.heading("cpu", text="CPU", anchor="w")
                self.table.heading("memory", text="RAM", anchor="w")
                self.table.heading("monitor", text="Monitor", anchor="w")
                self.table.heading("keyboard", text="Teclado", anchor="w")
                self.table.heading("mouse", text="Mouse", anchor="w")
                self.table.heading("power", text="Power", anchor="w")
                self.table.heading("diks", text="Diks", anchor="w")
                self.table.heading("motherboard", text="Motherboard", anchor="w")
                self.table.heading("person", text="Persona", anchor="w")

            case 'component':                
                self.table = ttk.Treeview(self.frame, columns=('type', 'data', 'id', 'computerid'), show="headings", xscrollcommand=self.hscroll.set)
                for col in self.table["columns"]:                                    
                    if col != "#0":                                                 
                        self.table.column(col, width=100, anchor="w")
                self.table.heading("type", text="Tipo", anchor="w")
                self.table.heading("data", text="Data", anchor="w")
                self.table.heading("id", text="ID", anchor="w")
                self.table.heading("computerid", text="ID Computadora", anchor="w")

        
        self.table.tag_configure("gray1", background="gray85")
        self.table.tag_configure("gray2", background="gray64")  
        