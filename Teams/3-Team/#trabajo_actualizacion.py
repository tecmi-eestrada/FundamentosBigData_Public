#trabajo
class Restaurante:

    # Inicialización
    def __init__(self, nombre, tipo_de_restaurante, fundacion):
        # Definición de atributos
        self.identidad = nombre
        self.tipo = tipo_de_restaurante
        self.ano_de_fundacion = fundacion
        self.mascota = "Dontaquito"
        self.platillos = ["tacos trompo", "tacos bistec", "campechanas", "gringas", "hamburguesas",
                          "frijoles especiales", "burrito", "tacos de carne asada", "tacos de suadero", "papa asada"]
        self.bebidas = ["fanta", "cocacola", "agua de limon", "boing de mango"]
        self.extras = ["queso", "guacamole", "doble carne", "frijoles a la charra", "papas a la francesa", "bbq", "buffalo", "ranch"]

    # Bienvenida
    def __str__(self):
        return f"Bienvenidos a {self.identidad} - {self.tipo}, fundado en el año {self.ano_de_fundacion}"
    #Retorna el menu
    def entrega_de_menu (self):
        menu = f"""
        bienvenidos a {self.identidad}
        menu 
        {self.platillos [0]}  """
        return menu

  # Crear instancia del restaurante
restaurante_loscoquettes = Restaurante("Los Coquettes", "Regional", "1888")

mimenu = restaurante_loscoquettes.entrega_de_menu ()
file_to_write = open("C:\\Users\\prisc\\Downloads\\codetrabajo\\trabajo_actualizacion.txt", "w")
file_to_write.write(mimenu)
file_to_write.close()
