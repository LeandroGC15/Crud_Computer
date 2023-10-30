"""
    System Add Computer v1.0
    Clase Computer que se encarga de crear computadoras en base de componente y asignarlos a personas
"""
import random, re   #Importando librerías random para generar IDs y re para el uso de expresiones regulares
random.seed(10)
#Creando la clase Computer
class Computer:
    def __init__(self, namePC, personCi):      #Inicializando la clase con los atributos de namePC y personCi
        self.namePC = namePC
        self.person = ''
        self.personCi = personCi
        self.id = self.generateId()             #Generando el ID
        self.components = ''        

        if self.personCi != '':                 #Evaluando que la ci no este vacia
            if "CI: " + self.personCi not in self.searchPerson():   #Evaluando si la persona existe en la lista de personas
                self.personCi = ''        
                print("La persona no existe. Se creará una computadora sin ser asignada a una persona.")
                print("Por favor, verifique la lista de personas que faltan.")     

        self.components = self.addComponent() #Agregando los componentes        

        if len(self.components) < 8:        #Evaluando si hay 8 componentes
            print("No se puede crear un computador con menos de 8 componentes.")
            print("Por favor, verifique la lista de componentes que faltan.")
        else:
            with open('db/computers.txt', 'a') as file:
                file.write(f'** Computador {self.namePC} **\n')
                file.write(f'ID: {self.id} -- {self.namePC}\n')
                file.write(f'Nombre ID Procesador Memoria Monitor Teclado Mouse Fuente Disco Placa Persona\n')
                file.write(f'[{self.namePC}, {self.id}, {self.components}, {self.person}]\n')
                file.write('*' * 30)
                file.write('\n')
                file.close()
                print(f'\n** Computador PC-{self.namePC} Creado **\n')
    
    def generateId(self):                       #Generador de IDs
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        length = len(numbers)
        id = ""
        for i in range(length):
            id += numbers[random.randint(0, length - 1)]
        return id

    def addComponent(self):                     #Agregando los componentes
        text = ''
        with open('db/components.txt', 'r') as file:
            text = file.read()
            file.close()
        
        #Buscando los componentes disponibless
        cpu_patron = r"\[Procesador,.\w+,.\w+,.\]"
        cpu_availables = re.findall(cpu_patron, text)  
        memory_patron = r"\[Memoria,.\w+,.\w+,.\]"
        memory_availables = re.findall(memory_patron, text)
        monitor_patron = r"\[Monitor,.\w+,.\w+,.\]"
        monitor_availables = re.findall(monitor_patron, text)
        keyboards_patron = r"\[Teclado,.\w+,.\w+,.\]"
        keyboards_availables = re.findall(keyboards_patron, text)
        mouse_patron = r"\[Mouse,.\w+,.\w+,.\]"
        mouse_availables = re.findall(mouse_patron, text)
        power_supply_patron = r"\[Fuente,.\w+,.\w+,.\]"
        power_supply_availables = re.findall(power_supply_patron, text)
        disk_patron = r"\[Disco,.\w+,.\w+,.\]"
        disk_availables = re.findall(disk_patron, text) 
        motherboard_patron = r"\[Placa,.\w+,.\w+,.\]"
        motherboard_availables = re.findall(motherboard_patron, text)     

        #Verificiando que los componentes esten disponibles
        if cpu_availables and memory_availables and monitor_availables and keyboards_availables and mouse_availables and power_supply_availables and disk_availables and motherboard_availables:

            cpu = cpu_availables[0].split(',')
            cpu = cpu[1]
            memory = memory_availables[0].split(',')
            memory = memory[1]
            monitor = monitor_availables[0].split(',')
            monitor = monitor[1]
            keyboards = keyboards_availables[0].split(',')
            keyboards = keyboards[1]
            mouse = mouse_availables[0].split(',')
            mouse = mouse[1]
            power_supply = power_supply_availables[0].split(',')
            power_supply = power_supply[1]
            disk = disk_availables[0].split(',')
            disk = disk[1]
            motherboard = motherboard_availables[0].split(',')
            motherboard = motherboard[1]

            #Asignando id del computador los componentes uno por uno
            #Para el procesador
            patron = r'\d{4,}'
            idComponent = re.findall(patron, cpu_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            #Memoria
            patron = r'\d{4,}'
            idComponent = re.findall(patron, memory_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            #Monitor
            patron = r'\d{4,}'
            idComponent = re.findall(patron, monitor_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            #Teclado
            patron = r'\d{4,}'
            idComponent = re.findall(patron, keyboards_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            #Mouse
            patron = r'\d{4,}'
            idComponent = re.findall(patron, mouse_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            #Fuente de poder
            patron = r'\d{4,}'
            idComponent = re.findall(patron, power_supply_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            #Disco
            patron = r'\d{4,}'
            idComponent = re.findall(patron, disk_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            #Placa base
            patron = r'\d{4,}'
            idComponent = re.findall(patron, motherboard_availables[0])
            patron = r''+idComponent[0]+',.\]'
            space = re.findall(patron, text)
            space = space[0].replace(' ', ' '+self.id)
            text = re.sub(patron, space, text)

            print(text)
            with open('db/components.txt', 'w') as file:
                file.write(text)
                file.close()

        else:
            print("No hay componentes disponibles, revisa la lista de componente.")
        
        components = [cpu, memory, monitor, keyboards, mouse, power_supply, disk, motherboard]
        return components
    
    def searchPerson(self):                    #Buscando la persona y le asiga una computadora
        text = ''
        with open('db/persons.txt', 'r') as file:
            text = file.read()
            file.close()

        patron1 = r"CI: " + self.personCi        
        ci = re.findall(patron1, text)
        name = ''
        patron2 = r"CI: "+self.personCi+" -- (\w+)"  

        name = re.findall(patron2, text)    
        if name:
            self.person = name[0]

        patron3 = r"\["+str(name)+"\w.+]"
        dataPerson = re.findall(patron3, text)

        data = ','.join(dataPerson)

        patron4 = r""+self.personCi+", ]"
        replace = r""+self.personCi+", "+self.namePC+", "+self.id+"]"
        new_text = re.sub(patron4, replace, data)

        text = text.replace(data, new_text)        

        with open('db/persons.txt', 'w') as file:
            file.write(text)
            file.close()
        return ci
        