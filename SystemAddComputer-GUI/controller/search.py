import re
#Este archivo es el encargado de buscar y validar si exite una persona, un computador o un componente. Ademas de actualizar y eliminar los datos de la persona, el computador o el componente.
def searchPerson(personCi='', option=None, **kwargs):       #Buscando la persona y le asiga una computadora
    text = ''                                               #Con **kwargs optemos los parametros ci, nombre, apellido, etc.
    with open('db/persons.txt', 'r') as file:
        text = file.read()
        file.close()

    if not text and option == None:                       #Si no hay personas registradas
        return False
    elif text == '' and option == 'read':
        print('No hay personas registradas')
        return False
    elif text and option == 'read':
        show = ''.join(text)
        print(show)
        return True

    patron1 = r'\*\* Persona \w+.\w+.\*\*\nCI:.'+personCi+'.--.\w+\n\w.+\n\[\w.+\n\*+'          #Buscando la persona con expresion regular por la cedula
    person = re.findall(patron1, text)

    if person:                                                  #Si la persona existe
        if option == 'update':                                  #Actualizando los datos de la persona si la opcion es update
            before = ''.join(person)

            patron2 = r"CI:.\d+.--.\w+"
            ci = re.findall(patron2, before)
            patron2 = r"\*\*.Persona.\w.+"
            header = re.findall(patron2, before)

            validIdComputer = searchComputer(kwargs['idComputer'])
            namePC, idPC = '', ''

            if not validIdComputer:
                p1 = r"\w[a-z]+,.\d{3,}"
                data = re.findall(p1, before)
                data = ','.join(data)
                data = data.split(',')
                namePC, idPC = data
            else:
                namePC = validIdComputer
                idPC = kwargs['idComputer']

            patron2 = r'\[\w.+]'
            listData = re.findall(patron2, before)
            after = before.replace(ci[0], "CI: "+kwargs['ci'] + ' -- ' + kwargs['firstName'])
            after = after.replace(header[0], "** Persona " + kwargs['firstName'] + ' ' + kwargs['lastName'] + " **")
            after = after.replace(listData[0], "[" + kwargs['firstName'] + ", " + kwargs['lastName'] + ", " + kwargs['age'] + ", " + kwargs['ci'] + ", "+namePC+", "+idPC+"]")
            print('\n'+after)
            text = text.replace(before, after)
            with open('db/persons.txt', 'w') as file:
                file.write(text)
                file.close()

            text2 = ''
            with open('db/computers.txt', 'r') as file:
                text2 = file.read()
                file.close()

            patron2 = r',.(\w+)]'
            name = re.findall(patron2, text2)
            if name:
                text2 = text2.replace(name[0], '-')

                patron2 = r''+idPC+',.\[\'\w.+(,.\])'
                space = re.findall(patron2, text2)
                text2 = text2.replace(space[0], ", " + name[0] + "]")
                with open('db/computers.txt', 'w') as file:
                    file.write(text2)
                    file.close()
                patron2 = r'\-\]'
                line = re.findall(patron2, text2)
                text2 = text2.replace(line[0], "]")
                with open('db/computers.txt', 'w') as file:
                    file.write(text2)
                    file.close()
            else:
                patron2 = r""+idPC+",.\[.*\w.+(,.\])"
                space = re.findall(patron2, text2)
                text2 = text2.replace(space[0], ", " + kwargs['firstName'] + "]")
                with open('db/computers.txt', 'w') as file:
                    file.write(text2)
                    file.close()

            print("\nPersona actualizada con exito\n")


        elif option == 'delete':
            before = ''.join(person)
            text = text.replace(before, '')
            with open('db/persons.txt', 'w') as file:
                file.write(text)
                file.close()
            text2 = ''
            with open('db/computers.txt', 'r') as file:
                text2 = file.read()
                file.close()

            patron2 = r',.\[\'\w.+,.(\w.+)\]'
            name = re.findall(patron2, text2)
            if name:
                text2 = text2.replace(name[0], '')
                with open('db/computers.txt', 'w') as file:
                    file.write(text2)
                    file.close()

            print("\nPersona eliminada con exito\n")
        else:
            print("\n")
            show = ' '.join(person)
            print(show)
    else:
        print("\nPersona no encontrada\n")
        return False
    
    return True

def searchComputer(idComputer='', option=None, **kwargs):
    text = ''
    with open('db/computers.txt', 'r') as file:
        text = file.read()
        file.close()

    if not text and option == None:
        return False
    
    elif text == '' and option == 'read':
        print('No hay computadoras registradas')
        return False
    elif text and option == 'read':
        show = ''.join(text)
        print(show)
        return True

    patron1 = r'\*\* Computador \w+.\w+.\*\*\nID:.'+idComputer+'.--.\w+\n\w.+\n\[\w.+\n\*+'      
    computer = re.findall(patron1, text)
    if computer:        
        if option == 'update':
            print("\n")
            show = ' '.join(computer)
            print(show)
            patron2 = r'Computador (\w+.\w+)'
            namePC_old = re.findall(patron2, computer[0])
            text = text.replace(namePC_old[0], kwargs['namePC'])
            with open('db/computers.txt', 'w') as file:
                file.write(text)
                file.close()
            print("\nComputador actualizado con exito\n")

        elif option == 'delete':
            before = ''.join(computer)
            patron2 = r'Computador (\w+.\w+)'
            namePC_old = re.findall(patron2, computer[0])
            text = text.replace(before, '')
            with open('db/computers.txt', 'w') as file:
                file.write(text)
                file.close()
            text2 = ''
            with open('db/persons.txt', 'r') as file:
                text2 = file.read()
                file.close()

            patron2 = r''+namePC_old[0]+',.'+idComputer+''
            name = re.findall(patron2, text2)

            if name:
                text2 = text2.replace(name[0], '')
                with open('db/persons.txt', 'w') as file:
                    file.write(text2)
                    file.close()

            print("\nPersona eliminada con exito\n")
        
        elif option == 'assign':
            text2 = ''
            with open('db/persons.txt', 'r') as file:
                text2 = file.read()
                file.close()

            patron = r'\*\* Persona (\w+.)'
            firstName = re.findall(patron, text2)

            text3 = ''
            with open('db/computers.txt', 'r') as file:
                text3 = file.read()
                file.close()
           
            patron = r'.*'+idComputer+'.*?(\w+)'        
            namePC = re.findall(patron, text3)

            patron1 = r'.*\nID:.'+idComputer+'.*\n.*\n.*'
            computer = re.findall(patron1, text3)

            patron2 = r''+idComputer+'.*?(,.\])'
            space = re.findall(patron2, text3)

            computer[0] = computer[0].replace(space[0], ", "+firstName[0] + "]")
            text3 = re.sub(patron1, computer[0], text3)

            with open('db/computers.txt', 'w') as file:
                file.write(text3)
                file.close()
            
            patron = r''+kwargs['personCi']+',(.)]'
            space = re.findall(patron, text2)
            print(space[0])
            space[0] = space[0].replace(space[0], kwargs['personCi'] + ", " + idComputer + "]")
            text2 = re.sub(patron, space[0], text2)

            with open('db/persons.txt', 'w') as file:
                file.write(text2)
                file.close()

        elif option == '':
            print("\n")
            show = ' '.join(computer)
            print(show)
    else:
        print("\nComputador no encontrado\n")
    
    patron2 = r'ID: '+idComputer+'.--.(\w+)'
    result = re.findall(patron2, text)
    namePC = ''
    if result:
        namePC = result[0]

    return namePC

def searchComponent(idComponent='', option=None, **kwargs):
    text = ''
    with open('db/components.txt', 'r') as file:
        text = file.read()
        file.close()
    
    if not text and option == None:
        return False
    elif text and option == None:
        return True
    elif not text and option == 'read':
        print('No hay componentes registrados')
        return False
    elif text and option == 'read':
        show = ''.join(text)
        print(show)
        return True

    patron1 = r'\*\* Componente \w.+\w+.\*\*\nID:.'+idComponent+'.--.\w.+\n\w.+\n\[\w.+\n\*+'        
    component = re.findall(patron1, text)
    if component:        
        if option == 'update':
            patron2 = r"Componente (\w+.\w+)"
            type_old = re.findall(patron2, component[0])
            text = text.replace(type_old[0], kwargs['type'])
            patron2 = r"ID:."+idComponent+".--.(\w+.\w+)"
            data_old = re.findall(patron2, component[0])
            text = text.replace(data_old[0], kwargs['data'])
            with open('db/components.txt', 'w') as file:
                file.write(text)
                file.close()
            print("\nComponente actualizado con exito\n")

        elif option == 'delete':
            before = ''.join(component)
            text = text.replace(before, '')
            with open('db/components.txt', 'w') as file:
                file.write(text)
                file.close()
            print("\nComponente eliminado con exito\n")
        else:
            print("\n")
            show = ' '.join(component)
            print(show)
    else:
        print("\nComponente no encontrado\n")
        return False
    
    return True
    

    

    