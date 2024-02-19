#Clase padre
class Persona:
    #---Atributos
    def __init__(self, nombre, apellido, edad, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.genero = genero
    
    #---Metodos
    def __str__(self):
        return f"Hola, me llamo {self.nombre} {self.apellido}, tengo {self.edad} años de edad y me identifico como {self.genero}"

    def presentacion_de_persona(self):
        saludo = f"Hola, me llamo {self.nombre} {self.apellido}, tengo {self.edad} años de edad y me identifico como {self.genero}"
        return saludo
    
    def saludar(self):
        print(self.presentacion_de_persona())

#---Objeto
# raul_hernandez = Persona("Raul", "Hernandez", 25, "Hombre")
# raul_hernandez.saludar()
# print(raul_hernandez)



#---Clase hijo con 
# class Estudiante(Persona):
#     pass

#---Objeto de clase hijo
# sandra_lopez = Estudiante("Sandra", "Lopez Saldaña", 32, "Mujer")
# print(sandra_lopez)

#---Definicion de clase gestionando la herencia
class Estudiante(Persona):

    #---Encapsulamiento
    # #public
    universidad = "TecMilenio"
    # # #protected
    # _universidad = "TecMilenio"
    # # #private
    # __universidad = "TecMilenio"

    #---Adicion de atributos exclusivos de la clase en el constructor
    def __init__(self, nombre, apellido, edad, genero, matricula, carrera, semestre, universidad=__universidad):
        # Persona().__init__(nombre, apellido, edad, genero)
        super().__init__(nombre, apellido, edad, genero)
        #---Definicion de atributos exclusivos de la clase 
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre
        # self.set_universidad(universidad)
        self.universidad = universidad

    def get_universidad(self):
        return self._universidad
    
    def set_universidad(self, value):
        self._universidad = value

    def __str__(self):
        # return super().__str__()
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y actualmente curso el {self.semestre} semestre de la carrera {self.carrera}"
    
    #---Polimorfismo
    def presentacion_de_persona(self):
        saludo = f"Hola, me llamo {self.nombre}, tengo {self.edad} años y actualmente curso el {self.semestre} semestre de la carrera {self.carrera} en {self.get_universidad()}"
        return saludo
    

simona_lamona = Estudiante("Simona", "Lamona", 17, "Mujer", 3025418, "IDS", "1er", "TecMilenio")
simona_lamona.saludar()
#------Acceder directo a atributos
#---Public
print(simona_lamona.universidad)
simona_lamona.universidad = "Tec de Monterrey"
print(simona_lamona.universidad)
#---Protected
# print(simona_lamona._universidad)
# simona_lamona._universidad = "UANL"
# print(simona_lamona._universidad)
#---Private
# print(simona_lamona.__universidad)
# simona_lamona.__universidad = "UNAM"
# print(simona_lamona.universidad)

#---Impresion de __str__ padre o hijo
# print(simona_lamona)