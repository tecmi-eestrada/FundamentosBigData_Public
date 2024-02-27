class Persona:
    #---Atributos
    def __init__(self, nombre, nombre2, apellido, apellido2, edad, genero):
        self.nombre = nombre
        self.nombre2 = nombre2
        self.apellido = apellido
        self.apellido2 = apellido2
        self.edad = edad
        self.genero = genero
    #---Metodos
    def __str__(self):
        return f"Hola, soy {self.nombre} {self.apellido}"

    def presentacion_de_persona(self):
        saludo = f"Hola, me llamo {self.nombre} {self.apellido}, tengo {self.edad} años de edad y me identifico como {self.genero}"
        return saludo
    
    def saludar(self):
        print(self.presentacion_de_persona())

nombre = "Marcia"
nombre2 = "Elisa"
apellido = "López"
apellido2 = "Huerta"
edad = "Diecinueve"
genero = "Mujer"

marcia = Persona(nombre, nombre2, apellido, apellido2,edad, genero)
print(marcia.nombre,marcia.nombre2,marcia.apellido,marcia.apellido2)
print(marcia)
marcia.saludar()