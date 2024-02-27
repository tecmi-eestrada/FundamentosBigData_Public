class JorgeGarza:
    def __init__(self, nombre, edad, ocupacion, rasgos):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
        self.rasgos = rasgos

    def mostrar_rasgos(self):
        print("Rasgos de", self.nombre + ":")
        for rasgo in self.rasgos:
            print(rasgo)

    def gustar_natacion(self):
        print(f"Me gusta hacer ejercicio, especialmente la natación en la cual destaque competitivamente.")
    
    def practicar_videojuegos(self):
        print(f"Ademas de destacar en la natacion, destaco en los videojuegos, jugando competitivamente para un equipo de esports.")


# Crear una instancia
mis_rasgos = ["Estatura: 1.76", "Aperlado", "Deportista"]
Yo_Jorge = JorgeGarza("Jorge Alejandro Garza Martinez", 20, "Ingeniero Industrial", mis_rasgos)

# Acceder a los atributos y mostrar los rasgos
print("Nombre:", Yo_Jorge.nombre)
print("Edad:", Yo_Jorge.edad)
print("Ocupación:", Yo_Jorge.ocupacion)
Yo_Jorge.mostrar_rasgos()
Yo_Jorge.gustar_natacion()
Yo_Jorge.practicar_videojuegos()