class Negocio:
    Nombre_Negocio = 'Gamer´s Speciatis'

    def __init__(self, Nombre_Negocio, tipo_de_restaurante, fundacion):
        # Definicion de atributos
        self.nombre = Nombre_Negocio
        self.tipo = tipo_de_restaurante
        self.fundacion = fundacion

        # Menu del Restaurante
        self.menu = 'Hamburguesa Sencilla, Hamburguesa Doble, Boneless, Alitas, Piratas, Burrote Gamer, Pizza Gamer, Nachos Supremos, Hot Dog, ChilaGamers'

        # Año de fundación
        self.fundacion = 1997

        # Nombre de la Mascota del restaurante
        self.Nombre_Mascota = 'Controlin'

    # Funcion que retorna la instancia con una cadena de texto
    def __str__(self):
        menu_str = "Menú de Platillos:\n"
        for platillo in self.Menu_Platillos:
            menu_str += f"{platillo['Nombre']}: {platillo['Descripcion']} - Precio: ${platillo['Precio']}\n"
        
        menu_str += "\nMenú de Bebidas:\n"
        for bebida in self.Menu_Bebidas:
            menu_str += f"{bebida['Nombre']}: {bebida['Descripcion']} - Precio: ${bebida['Precio']}\n"
        
        return f"Bienvenidos a {self.Nombre_Negocio}, fundado en el año {self.fundacion}\n{menu_str}"
    

    # Menú de platillos
    Menu_Platillos = [
        {"Nombre": "Hamburguesa Sencilla", "Descripcion": "Carne de res, lechuga, tomate, queso cheddar, salsa especial, en pan de hamburguesa", "Precio": 75},
        {"Nombre": "Hamburguesa Doble", "Descripcion": "Doble Carne de res, lechuga, salchicha, aros de cebolla, tomate, queso cheddar, salsa especial, en pan de hamburguesa", "Precio": 120},
        {"Nombre": "Pizza Gamer", "Descripcion": "Pepperoni, salsa de tomate, queso mozzarella, en masa Romana", "Precio": 120},
        {"Nombre": "Alitas", "Descripcion": "Alitas de pollo bañadas en tu salsa preferida, acompañadas bastones de apio", "Precio": 85},
        {"Nombre": "Nachos Supreme", "Descripcion": "Totopos de maíz, carne molida, queso fundido, guacamole, y crema", "Precio": 75},
        {"Nombre": "Hot Dog", "Descripcion": "Salchicha de res, cebolla caramelizada, mostaza, kétchup, en pan de hot dog", "Precio": 65},
        {"Nombre": "Pirata", "Descripcion": "Carne Asada, queso rallado, aguacate, en su tortilla de arina", "Precio": 140},
        {"Nombre": "Burrote Gamer", "Descripcion": "Tortilla de harina rellena de carne de res deshebrada, frijoles, queso, y crema", "Precio": 180},
        {"Nombre": "Papas Fritas Especiales", "Descripcion": "Papas fritas crujientes sazonadas con sal y pimiento al gusto, queso fundido , y trocitos de tocino", "Precio": 99},
        {"Nombre": "ChilaGamers", "Descripcion": "Tortilla de maiz crujiente, salsa verde o roja, queso garatinado, cama de frijoles, y cecina de res ", "Precio": 80},
    ]

    # Menú de bebidas
    Menu_Bebidas = [
        {"Nombre": "Refrescos", "Descripcion": "Coca Cola, Sprite, Fanta, Topo Chico, Mundet, y Doctor Pepper", "Precio": 25},
        {"Nombre": "Aguas de Sabor", "Descripcion": "Agua de Jamaica, Limon, Mango, Horchata, y Fresa", "Precio": 20},
        {"Nombre": "Bebidas alcoholicas", "Descripcion": "Heineken, Tecate, Carta Blanca, Indio, Budweiser", "Precio": 85},
        {"Nombre": "Agua", "Descripcion": "Agua embotellada", "Precio": 20}
    ]

# Crear una instancia de la clase Negocio
mi_negocio = Negocio("Gamer´s Speciatis", "Restaurante", 1997)
# Imprimir la instancia
print(mi_negocio)

file_to_write = open("C:\\Users\\paty_\\OneDrive\\Documentos\\TECMI\\Negocio.txt", "w")
file_to_write.write(str(mi_negocio))
file_to_write.close ()
