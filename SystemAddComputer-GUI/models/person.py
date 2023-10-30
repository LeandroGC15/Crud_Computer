"""
    System Add Computer v1.0
    Clase Person para la creación de las personas y guardarlas en un archivo persons.txt
"""
#Creando la clase Person
class Person:
    def __init__(self, firstName, lastName, age, ci): 
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.ci = ci

        with open('db/persons.txt', 'a') as file:
            file.write(f'** Persona {self.firstName} {self.lastName} **\n')
            file.write(f'CI: {self.ci} -- {self.firstName}\n')
            file.write(f'Nombre Apellido Edad CI Computadora\n')
            file.write(f'[{self.firstName}, {self.lastName}, {self.age}, {self.ci}, ]\n')
            file.write('*' * 30)
            file.write('\n')
            file.close()