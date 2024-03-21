class Javier():
    def __init__(self, carrera,nombre, edad, altura, ejercicio, tiempo_libre, pasear, festivales, estadio):
        self.carrera = carrera
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.ejercicio = ejercicio
        self.tiempo_libre = tiempo_libre
        self.pasear = pasear
        self.festivales = festivales
        self.estadio = estadio

    def practicar_deportes(self):
        print(f"Me gustaria practicar alguna arte marcial")

    def viajar(self):
        print(f"Uno de mis obejtivos es viajar por todo el mundo e ir conociendo las maravillas del mundo.")

    def fundacion_perritos(self):
        print(f"Me gustaria en un futuro no muy lejano poder tener alguna fundación para poder salvar perritos y conseguirles una mejor vida.")

    def presentacion(self) -> str:
        return f''' Hola mi nombre es {self.nombre} tengo {self.edad} años, mido {self.altura} me gusta hacer {self.ejercicio}, 
        en mis tiempos libres me pongo a {self.tiempo_libre} videojuegos o  {self.pasear} a mis mascotas.
        Mi pasatiempo favorito es ir a {self.festivales}, e ir al {self.estadio}'''

mio_Javi = Javier("enfermeria", "O. Javier Hernández Rivera", 27, 1.83, "todo tipo de ejercicio", "jugar", "pasear", "festivales de musica", "estadio")
print(mio_Javi.presentacion())