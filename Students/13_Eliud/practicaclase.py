class Eliud:
    def __init__(self, nombre, edad, color_piel, pais, apodo, video_juegos, comida, estatura):
        self.nombre = nombre
        self.edad = edad
        self.color_piel = color_piel
        self.pais = pais
        self.apodo = apodo
        self.video_juegos = video_juegos
        self.estatura = estatura
        self.comida = comida

    def datos(self) -> str:
        return f''' Hola mi nombre es {self.nombre} tengo {self.edad} años de edad, soy originario de {self.pais} 
 y la gente cercana me conoce como {self.apodo}'''
   
    def hobbys(self) -> str:
        return f''' Algunos de mis pasatiempos es jugar videojuegos como seria {self.video_juegos} 
 ademas de vivir la vida loca'''   

    def datos_extra(self) -> str:
        return f''' Mi estatura es {self.estatura} mi tez es {self.color_piel} ademas de tener un gran gusto por la {self.comida}
 y la cerveza'''

eliud= Eliud("Jorge Eliud Ramos Hernandez", 20, "aperlada", "México", "Mahui", "LoL, Warframe, Fortnite, Minecraft y COD", "Carne Asada", 1.76 )
print(eliud.datos())
print(eliud.hobbys())
print(eliud.datos_extra())