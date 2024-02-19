#ORIENTADO_A_OBJETOS

#definimos clase

class Restaurante:

    platillos = {'platillo' : '120',}
    def __init__(self, nombre, tipo_comida, Año_fundacion, mascota):
        self.nombre = nombre 
        self.TipoComida = tipo_comida
        self.fundacion = Año_fundacion
        self.mascota = mascota
        
    def __str__(self):
        return f"Bienvenidos a {self.nombre}, nuestro tipo de comida es {self.TipoComida} y estamos llenando barrigas desde {self.fundacion}"
    def Entrega_Menu(self):
        platillos = f"""
                Este es nuestro Menu
        {self.platillos}--------{self.platillos['platillo']}
            (Ingredientes: Arroz Gohan, Alga, Aguacate, Queso Crema, Camaron) (200 gr)
        Rollo Cristiano----------------$140 
            (Ingredientes: Arroz Gohan, Agua Bendita) (200 gr)
        Rollo Jamaiquino---------------$100
            (Ingredientes: Arroz Gohan, Alga, Jamaica) (200 gr)
        Tempura------------------------$30/pz 
            (Ingredientes: Camaron Empanizado) (50 gr)
        Arroz Frito--------------------$100 
            (Ingredientes: Arroz Frito (Puedes incluir extras)) (300 gr)
        Ramen--------------------------$200 
            (Ingredientes: Fideos Maruchan (Sujeto a Extras)) (200 gr)
        Rollo Maki---------------------$120 
            (Ingredientes: Arroz Gohan, Pescado en Escabeche) (200 gr)
        Rollo Temaki-------------------$50
            (Ingredientes: Arroz Gohan, Pescado en Escabeche) (200 gr)
        Rollo Hosomaki-----------------$150
            (Ingredientes: Arroz Gohan, Pescado en Escabeche) (200 gr)
        Onigiri Tilapia----------------$70
            (Ingredientes: Filete de Tilapia, Alga Marina, Arroz Gohan) (100 gr)
        Onigiri Atún-------------------$100
            (Ingredientes: Atun Magro, Alga Marina, Arroz Gohan) (100 gr)
                """
        return platillos
    def Entrega_Bebidas(self):
        bebidas = f"""
            Estas Son Nuestras Bebidas
        Coca Cola-----------------$200 (350 ml)
            (Ingredientes: Agua carbonatada, Azucar, Jarabe de Maiz)
        Limonada------------------$70 (Refill) (500 ml)
            (Ingredientes: Agua, Limon, Azucar)
        Agua de Fresa-------------$100 (500 ml)
            (Ingredientes: Agua, Fresa, Azucar)
        Fanta --------------------$50 (350 ml)
            (Ingredientes: Agua carbonatada, Azucar, Jarabe de Naranja, Extracto de Naranja Artificial)
        Sprite--------------------$50 (350 ml)
            (Ingredientes: Agua carbonatada, Azucar, Jarabe de Limon, Cascara de Limon, Cascaras de Citricos)

                """
        return bebidas
    def Entrega_Extras(self):
        extras = f"""
            Estos Son Nuestros Extras
        Pollo-----------------------------------$100 (200 gr)
            (Ingredientes: Pollo) 
        Verduras Fritas-------------------------$30  (250 gr)
            (Ingredientes: Zanahoria, Brocoli, Lechuga, Cebolla) 
        Carne de Res----------------------------$100 (200 gr)
            (Ingredientes: Wagyu A5) 
        Salsa de Anguila -----------------------$30  (100 ml)
            (Ingredientes: Extracto de Anguila) 
        Salsa Soja------------------------------$100 (100 ml)
            (Ingredientes: Raices Mixtas) 
        Salsa Sambal----------------------------$20  
            (Ingredientes: Sambalina de Rio de Janeiro) (200 gr)
        Aderezo Chipotle------------------------$12  
            (Ingredientes: Chipotle, Mayonesa, Limon)
        Salsa Sriracha--------------------------$50  (100 ml)
            (Ingredientes: Sriracha) 
        Mixto-----------------------------------$150 (250 gr)
            (Ingredientes: Carne de Res, Pollo, Verduras Fritas) 
        
                """
        return extras
    def Entrega_Combo(self):
        extras = f"""
            Estos Son Nuestros Extras
        Combo Paquetellenes----------------------$520
            (Incluye: Rollo California $120 - Arroz Frito $100 - Ramen $200 - Limonada $70 - Salsa Soja $100) 
        Combo Casiqueado-------------------------$230
            (Incluye: Arroz Frito $100  - Onigiri Atun $100 - Coca Cola $50 )  
        Combo MejorNadota------------------------$300 
            (Incluye: Rollo Osomaki $150 - Onigiri Tilapia $70 - Arroz Frito $100 ) 
        
        
                """
        return extras
NuestroRestaurante = Restaurante("PollitoAnabolico", "Oriental", 2002, "Mapache")

#desplegamos mensaje de bienvenida
print(NuestroRestaurante)
print(NuestroRestaurante.Entrega_Menu())
print(NuestroRestaurante.Entrega_Extras())
print(NuestroRestaurante.Entrega_Bebidas())
print(NuestroRestaurante.Entrega_Combo())

Respuesta = print(str(input("Que desea pedir")))
print(Respuesta)





#creamos menu para que el usuario despliegue el menu








