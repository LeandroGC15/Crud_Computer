"""
    System Add Computer v1.0
    index.py - Controlador clases y funciones de la aplicación
"""
#Importando cada clase que se encuentran en la carpeta models
from models.person import *
from models.computer import *
from models.components import *
from .search import *               #Importando la funcion para buscar
import time                         #Importando la librería time para usar delays

#Creando la clase Controller
class Controller:
    def __init__(self, option):
        self.option = option
    
    def create(self):                               #Método para crear
        match self.option:
            case 'person':                          #Creando una persona
                print("Creando una persona")
                firstName = input("Nombre: ")
                lastName = input("Apellido: ")
                age = input("Edad: ")
                ci = input("CI: ")
                person = Person(firstName, lastName, age, ci)
                print(f'\n** Persona {person.firstName} Creada **\n')
                time.sleep(1)

            case 'computer':                        #Creando un computador
                print("Creando un computador")
                namePC = input("Nombre para la computadora: PC-")
                exists_component = searchComponent()

                if exists_component:
                    add = input("Asignar a una persona?[s/n]: ")   
                    match add:                          #Evaluando si se desea asignar una computadora
                        case 's':
                            ci = input("CI de la persona: ")
                            computer = Computer(namePC, ci)
                            if computer.personCi not in computer.searchPerson():
                                pass
                            time.sleep(1)
                        case 'n':
                            ci = ''
                            computer = Computer(namePC, ci) 
                            time.sleep(1)   
                        case other:
                            print("Opcion incorrecta")
                else:
                    print("No hay componentes disponibles")
                    time.sleep(1)         

            case 'component':                       #Agregando un componente
                print("""Agregando un componente
** Tipo de componente **

[1] Procesador
[2] Memoria
[3] Disco Duro
[4] Placa Madre
[5] Fuente de poder
[6] Teclado
[7] Mouse
[8] Monitor
[0] Atras\n""")
                
                option = int(input('> '))       #Preguntando al usuario que tipo de componente desea agregar

                match option:                     #Evaluando la opción seleccionada
                    case 1:
                        type = "Procesador"
                        print("\nAgregando un procesador\n")
                        data = input("Modelo: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)

                    case 2:
                        type = "Memoria"
                        print("\nAgregando una memoria\n")
                        data = input("Gigabytes: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)
                    case 3:
                        type = "Disco"
                        print("\nAgregando un disco\n")
                        data = input("Capacidad: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)

                    case 4:
                        type = "Placa"
                        print("\nAgregando una placa base\n")
                        data = input("Modelo: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)

                    case 5:
                        type = "Fuente"
                        print("\nAgregando una fuente de poder\n")
                        data = input("Potencia: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)

                    case 6:
                        type = "Teclado"
                        print("\nAgregando un teclado\n")
                        data = input("Modelo: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)

                    case 7:
                        type = "Mouse"
                        print("\nAgregando un mouse\n")
                        data = input("Modelo: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)

                    case 8:
                        type = "Monitor"
                        print("\nAgregando un monitor\n")
                        data = input("Modelo: ")
                        component = Components(type, data)
                        print(f'\n** Componente {component.type} - {component.data} Agregado **\n')
                        time.sleep(1)

                    case 9:                     #No agregar nada y volver al menú principal
                        print()
                    case other:
                        print("Opción no válida")
            case other:
                print("Error")

    def read(self):                             #Mostrando los datos
        match self.option:
            case 'person':                          #Mostrando personas
                print("\nListado de personas\n")
                searchPerson(option='read')
                """ persons = ''
                
                with open("db/persons.txt", "r") as file:
                    persons += file.read()
                    file.close()
                print(persons) """

            case 'computer':                        #Mostrando computadoras
                print("\nListado de computadoras\n")                
                searchComputer(option='read')

            case 'component':                       #Mostrando componentes
                print("\nListado de componentes\n")
                searchComponent(option='read')
                

    def update(self):                               #Actualizando datos
        match self.option:
            case 'person':                          #Actualizando una persona
                print("\nActualizar datos de una persona\n")
                ci = input("CI de la persona: ")                
                exists = searchPerson(ci)           #Buscando la persona
                if exists:                          #Si la persona existe
                    new_firstName = input("Nombre: ")
                    new_lastName = input("Apellido: ")
                    new_age = input("Edad: ")
                    new_ci = input("CI: ")
                    new_idComputer = input("ID del computador: ")
                    searchPerson(ci, 'update', firstName=new_firstName, lastName=new_lastName, age=new_age, ci=new_ci, idComputer=new_idComputer) #Actualizando los datos
                
            case 'computer':                        #Actualizando un computador
                print("\nActualizando un computador\n")
                idComputer = input("ID del computador: ")
                exists = searchComputer(idComputer) #Buscando el computador
                if exists:                          #Si el computador existe
                    new_namePC = input("PC-: ")
                    searchComputer(idComputer, 'update', namePC=new_namePC) #Actualizando el nombre

            case 'component':                       #Actualizando un componente
                print("\nActualizando un componente\n")
                idComponent = input("ID del componente: ")
                exists = searchComponent(idComponent)   #Buscando el componente
                if exists:                              #Si el componente existe
                    new_type = input("Tipo de componente: ")
                    new_data = input("Modelo: ")
                    searchComponent(idComponent, 'update', type=new_type, data=new_data)#Actualizando los datos
            case other:
                print("Error")

    def delete(self):                           #Eliminar datos
        match self.option:
            case 'person':                          #Borrando una persona
                print("Eliminar una persona")
                ci = input("CI de la persona: ")                
                exists = searchPerson(ci)
                if exists:
                    searchPerson(ci, 'delete')
            case 'computer':                        #Borrando un computador
                print("Eliminar un Computador")
                idComputer = input("ID del computador: ")                
                exists = searchComputer(idComputer)
                if exists:
                    searchComputer(idComputer, 'delete')
            case 'component':                       #Borrando un componente
                print("Eliminar un Componente")
                idComponent = input("ID del componente: ")           
                exists = searchComponent(idComponent)
                if exists:
                    searchComponent(idComponent, 'delete')
            case other:
                print("Error")

    def search(self):                               #Buscando datos específicos
        match self.option:
            case 'person':                          #Buscando una persona
                print("\nBuscando una persona\n")
                searchPerson(input("CI de la persona: "))
            case 'computer':                        #Buscando un computador
                print("\nBuscando un computador\n")
                searchComputer(input("ID del computador: "), '')
            case 'component':                       #Buscando un componente
                print("\nBuscando un componente\n")
                searchComponent(input("ID del componente: "))
            case other:
                print("Error")
    
    def assignComputer(self):                      #Asignando un computador
            print("\nAsignando un computador a una persona\n")
            personCi = input("CI de la persona: ")
            exists = searchPerson(personCi)
            if exists:                            #Si la persona existe
                computers = ''
                print("\nListado de computadoras\n")                #Mostrando las computadoras
                with open("db/computers.txt", "r") as file:
                    computers += file.read()
                    file.close()
                print(computers)
                idComputer = input("ID del computador que desea asignar: ")         #Buscando el computador
                exists_computer = searchComputer(idComputer)
                if exists_computer:
                    searchComputer(idComputer, 'assign', personCi=personCi)
                    print("Computador asignado")
                
    