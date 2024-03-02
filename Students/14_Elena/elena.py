class ElenaReyes:
    def __init__(self,nombre,apellido,color_favorito,hobbie,deporte,musica,cancion) -> None:
        self.nombre=nombre
        self.apellido=apellido
        self.color_favorito=color_favorito
        self.hobbie=hobbie
        self.deporte=deporte
        self.musica=musica
        self.cancion=cancion
    def __str__(self):
        return f"Hola, me llamo {self.nombre} {self.apellido}, {self.color_favorito} {self.hobbie}"

    def presentacion_de_persona(self):
        saludo = f"Hola, me llamo {self.nombre} {self.apellido}, {self.color_favorito} {self.hobbie}. {self.musica} {self.cancion}"
        return saludo

    def saludar(self):
        print(self.presentacion_de_persona())

nombre= "Elena"
apellido="Reyes"
Color_favorito ="Mi color favorito es el negro, "
hobbie="mi hobie es escuchar musica, "
Deporte="mi deporte favorito es el tenis de mesa."
Musica="La musica que más he escuchado es del grupo de Cuarteto de Nos, "
Cancion="y la cancion que más me gusta de ellos es Tiburones en el bosque"

elena=ElenaReyes(nombre,apellido,Color_favorito,hobbie,Deporte,Musica,Cancion)
elena.saludar()
print(elena.nombre,elena.apellido)
print(elena)
