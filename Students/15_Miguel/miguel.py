class Cipriano:
    def __init__(self, nombre, edad, colorPiel, altura, ejercicio, juegos, estudiar):
        self.nombre = nombre
        self.edad = edad
        self.colorPiel = colorPiel
        self.altura = altura
        self.ejercicio = ejercicio
        self.juegos = juegos 
        self.estudiar = estudiar

    def presentacionEquis(self):

        return f'''Hola que tal, soy {self.nombre}, tengo {self.edad}, desgraciadamente mi color de piel es {self.colorPiel} y mi altura es de {self.altura}'''

    def decirHobbie(self):

        return f'''Tambien puedo decir que aunque tenga {self.edad} años y mida {self.altura} metros aun puedo hacer {self.ejercicio} y cargar mucho'''

    def rendimientoJuegos(self):

        return f'''Y desgraciadamente pierdo mi tiempo jugando {self.juegos}, realmente a mis {self.edad} años no deberia estar haciendo estas cosas y me arrepiento mucho, podria pasar mas de ese tiempo {self.estudiar} Estructura de Datos'''

    def fumar(self):

        return f'''Y alchile me gusta mucho fumar a mis {self.edad}, te lo juro que lo puedo dejar cuando yo quiera pero me encanta hacerlo y no afecta mi rendimiento a la hora de hacer {self.ejercicio} pero si me incita a jugar {self.juegos}'''




NiñoMenso = Cipriano("Miguel", 21, "Guero", 1.65, "Pesas", "League of Legends", "Estudiando")

print(NiñoMenso.presentacionEquis())  
print(" ")
print(NiñoMenso.decirHobbie())
print(" ")
print(NiñoMenso.rendimientoJuegos())
print(" ")
print(NiñoMenso.fumar())

