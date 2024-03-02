class Roberto:
    def __init__(self):
        self.nombre = "Roberto"
        self.apellido = "Elizondo"
        self.edad = 22
        self.mascota = "Kira"

    def registrar_roberto(self) -> dict:
        dic_nombre = {
            "nombre": self.nombre,
            "apellido": self.apellido,
            "edad": self.edad,
            "mascota": self.mascota
        }
        return dic_nombre

    def datos_roberto(self) -> str:
        return f'''Hola, soy {self.nombre} mi apellido es {self.apellido}. Tengo {self.edad} años. No olviden saludar a mi mascota {self.mascota}!'''


roberto = Roberto()


print(roberto.datos_roberto())
print(roberto.registrar_roberto())