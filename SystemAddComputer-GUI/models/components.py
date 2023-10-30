"""
    System Add Computer v1.0
    Clase Componentes que ayuda a la creación de los componentes y guardarlos en un archivo components.txt
"""
import random       #Importando la librería random para usar numeros aleatorios y generar IDs
import os           #Importando la librería os para usar os.path
import re           #Importando la librería re para el uso de expresiones regulares
random.seed(10)
#Creando la clase Components
class Components: 
    def __init__(self, type, data):     #Inicializando la clase con los atributos de tipo y data
        self.type = type
        self.data = data
        self.id = self.generateId()   #Generando el ID

        if os.path.exists('db/components.txt'): #Evaluando si el archivo components.txt existe
            with open('db/components.txt', 'r') as file:
                text = file.read()
                file.close()
            
            patron = r"\*+.\w+.("+self.type+")"
            search_type = re.findall(patron, text)

            if search_type:
                patron = r"\*+.\w+."+self.type+".*?\n\w.+\n-\n"
                selects_componets = re.findall(patron, text)
                patron2 = r"\-\n"
                add_componets = re.findall(patron2, selects_componets[0])
                new_componets = selects_componets[0].replace(add_componets[0], f"-\n[{self.type}, {self.data}, {self.id}, ]\n")
                patron2 = r"\*\* Componente "+self.type+" \*\*.*\n\w.+\n\w.+\n\[\w.+\n*?-"

                text = re.sub(patron, new_componets, text)

                with open('db/components.txt', 'w') as file:
                    file.write(text)
                    file.close()
            else:
                self.create()
        else:
            self.create()

    def generateId(self):                                   #Generador de IDs
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        length = len(str(self.type))
        id = ""
        for i in range(length):
            id += str(numbers[random.randint(0, length - 1)])
        return id

    def create(self):
        with open('db/components.txt', 'a') as file:        #Agregando el componente al archivo components.txt
                file.write(f'** Componente {self.type} **\n')
                file.write(f'Tipo Data ID ComputadoraIDAsociada\n')
                file.write('-\n')
                file.write(f'[{self.type}, {self.data}, {self.id}, ]\n')                
                file.write('*' * 30)
                file.write('\n')
                file.close()