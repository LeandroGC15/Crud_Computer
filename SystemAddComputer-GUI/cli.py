"""
    System Add Computer v1.0
    main.py - Iniciador de la aplicación
"""
#Imporatando todas las clases que están en la carpeta models
import warnings                     #Importando la librería warnings
warnings.filterwarnings("ignore")   #Ignorando las advertencias

from controller.index import *
import os

#Creando la función para el menú de opciones
def menu():
    print('-' * 30) #Dibujando una línea
    print("\tMenú de Opciones\n" + '-' * 30)
    print("""
[1] Administrar personas
[2] Administrar computadores
[3] Administrar componentes
[0] Salir\n""")
    print('-' * 30)

    option = int(input('> '))   #Preguntando al usuario que opcion desea

    match option:               #Evaluando la opción seleccionada
        case 0:
            print('Saliendo del programa...')
            os.system('pause')
        case 1:
            clear()
            menuPersons()
        case 2:
            clear()
            menuComputers()
        case 3:
            clear()
            menuComponents()
        case other:
            invalidOption()
            menu()

def menuPersons():
    print('-' * 30) #Dibujando una línea
    print("\tMenú de Personas\n" + '-' * 30)
    print("""
[1] Crear persona
[2] Mostrar personas
[3] Actualizar persona
[4] Eliminar persona
[5] Buscar persona
[6] Atras
[7] Asignar computadora
[0] Salir\n""")
    print('-' * 30)

    option = int(input('> '))   #Preguntando al usuario que opción desea

    selectOption(option, 'person') #Evaluando la versión seleccionada

def menuComputers():
    print('-' * 30) #Dibujando una línea
    print("\tMenú de Computadores\n" + '-' * 30)
    print("""
[1] Crear computador
[2] Mostrar computadoras
[3] Actualizar computador
[4] Eliminar computador
[5] Buscar computador
[6] Atras
[0] Salir\n""")
    print('-' * 30)

    option = int(input('> '))   #Preguntando al usuario que opción desea

    selectOption(option, 'computer') #Evaluando la versi¢n seleccionada

def menuComponents():
    print('-' * 30) #Dibujando una línea
    print("\tMenú de Componentes\n" + '-' * 30)
    print("""
[1] Agregar componente
[2] Mostrar componentes
[3] Actualizar componente
[4] Eliminar componente
[5] Buscar componente
[6] Atras
[0] Salir\n""")
    print('-' * 30)

    option = int(input('> '))   #Preguntando al usuario que opción desea

    selectOption(option, 'component') #Evaluando la versi¢n seleccionada

def selectOption(option, model):                #Selector de opción
    match option:               #Evaluando la opción seleccionada
        case 0:
            print('Saliendo del programa...')
            os.system('pause')
        case 1:
            clear()
            Controller(model).create()          #llamando al controlador de crear
        case 2:
            clear()
            Controller(model).read()            #llamando al controlador de mostrar
        case 3:
            clear()
            Controller(model).update()          #llamando al controlador de actualizar
        case 4:
            clear()
            Controller(model).delete()          #llamando al controlador de eliminar
        case 5:
            clear()
            Controller(model).search()          #llamando al controlador de buscar
        case 6:
            clear()                    #Regresando al menú principal
            menu()
        case 7:
            clear() 
            Controller(model).assignComputer()
        case other:
            invalidOption()                     #Mensajes de error
            menu()
    menu()

def invalidOption():                #Mensajes de error
    print('Opción incorrecta. Presione para una tecla continuar...')
    os.system('pause')
    clear()

def clear():                        #Limpieza de consola
    if os.name == 'nt':     #Limpiando la consola en Windows
        os.system('cls')
    else:                    #Limpiando la consola en Linux o Mac
        os.system('clear')

menu()                                #Llamando al menú principal