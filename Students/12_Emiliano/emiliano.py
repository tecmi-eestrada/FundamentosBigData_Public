class  Emiliano_Navarro_Ramos:
    def __init__(self, nombre, edad, ojos, pelo, barba):
        self.nombre = nombre 
        self.edad = edad
        self.ojos = ojos
        self.pelo = pelo
        self.barba = barba

    def videojuegos(self):
        print("Me gusta bastante jugar videojuegos")

    def futbolamericano(self):
        print("Me gusta mucho ver futbol americano")

    def Anime(self):
        print("Me gusta ver anime")

emiliano = Emiliano_Navarro_Ramos("Emiliano Navarro Ramos", 18, "café", "café", "negra con pelirroja")
print("Nombre ", emiliano.nombre )
print("Edad ", emiliano.edad)
print("Mi color de ojos es ", emiliano.ojos)
print("Mi color de pelo", emiliano.pelo)
print("Mi color de barba es", emiliano.barba)
emiliano.videojuegos()
emiliano.futbolamericano()
emiliano.Anime()