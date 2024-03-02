class Fernanda: 
    def __init__(self, nombre, edad, pais, genero, frase,deporte, gustos, personalidad, carrera,escuela, mariscos, pasta, asiatica):
        self.nombre = nombre
        self.edad = edad
        self.pais= pais 
        self.genero= genero 
        self.frase= frase
        self.personalidad= personalidad 
        self.carrera=carrera
        self.escuela= escuela
        self.deporte= deporte
        self.gustos= gustos
        self.mariscos= mariscos
        self.pasta= pasta 
        self.asiatica= asiatica

    def introduction(self):
        return f'''Hola mi nombre es {self.nombre} tengo {self.edad} años, soy de {self.pais} y soy del genero {self.genero}. Mi frase favorita es {self.frase} y soy una persona muy {self.personalidad}.Estudio la {self.carrera} en {self.escuela}.'''
    def ejercicio (self): 
        return f"Me gusta mucho jugar {self.deporte} y {self.gustos}."
    def comida(self):
        return f"Mi comida favorita son los {self.mariscos}, todo tipo de {self.pasta} y el {self.asiatica}"

misAtributos=Fernanda("Maria Fernanda Galindo Castillo", 19, "México","femenino","todo es parte del proceso", "voleibol","bailar",
                       "risueña", "ingenieria industrial", "Tecmielnio","mariscos", "pastas","sushi")
print(misAtributos.introduction())
print(misAtributos.ejercicio())
print(misAtributos.comida())