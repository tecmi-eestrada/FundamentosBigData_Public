import pandas as pd

class Restaurante:
    def __init__(self, nombre, tipo_de_restaurante, fundacion, mascota):
        self.identidad = nombre
        self.tipo = tipo_de_restaurante
        self.ano_de_fundacion = fundacion
        self.mascota = "Dontaquito"
        def datos_restaurante(self) -> str:
                return f'''Bienvenidos a {self.nombre} donde nuestra comida estilo {self.tipo_comida} 
                        ha hecho felices a miles de familias desde {self.fundacion}. 
                        No olviden saludar a nuestra mascota {self.mascota}!'''

class Productos:
    def __init__(self, nombre, descripcion, precio:float):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    #Metodo crear_menu
    #input  - Documento csv
    #output - Menu estructurado (platillos, bebidas, extras, combos)
    def crear_menu(self, menu_doc):
        pass

    #Metodo registrar_platillos
    #input  - platillo = lista de objetos de platillo
    #output - lista de diccionarios de platillos
    def registrar_platillos(self, platillos) -> list:
        output = []
        for platillo in platillos:
            dic_platillo = {
                "platillo": platillo.nombre,
                "descripcion": platillo.descripcion,
                "precio": platillo.precio
            }
            output.append(dic_platillo)
        print(f'registro de {len(platillos)} Platillos al menu fue exitoso')
        return output

    #Metodo registrar_platillos
    #input  - bebida = lista de objetos de bebida
    #output - lista de diccionarios de bebidas
    def registrar_bebida(self, bebidas) -> list:
        output = []
        for bebida in bebidas:
            dic_bebida = {
                "bebida": bebida.nombre,
                "descripcion": bebida.descripcion,
                "precio": bebida.precio
            }
            output.append(dic_bebida)
        print(f'registro de {len(bebidas)} Bebidas al menu fue exitoso')
        return output

    #Metodo registrar_platillos
    #input  - extra = lista de objetos de extra
    #output - lista de diccionarios de extras
    def registrar_extra(self, extras) -> list:
        output = []
        for extra in extras:
            dic_extra = {
                "extra": extra.nombre,
                "descripcion": extra.descripcion,
                "precio": extra.precio
            }
            output.append(dic_extra)
        print(f'registro de {len(extras)} Extras al menu fue exitoso')
        return output
    
    #Metodo registrar_platillos
    #input  - combo = lista de objetos de combo
    #output - lista de diccionarios de combos
    def registrar_combos(self, combos) -> list:
        output = []
        for combo in combos:
            dic_combo = {
                "combo": combo.nombre,
                "platillo": combo.platillo,
                "bebida": combo.bebida,
                "extra": combo.extra,
                "descripcion": combo.descripcion,
                "precio": combo.precio
            }
            output.append(dic_combo)
        print(f'registro de {len(combos)} Combos al menu fue exitoso')
        return output
    
    #Metodo crear_combo
    #input  - platillo = objeto platillo
    #       - bebida = objeto bebida        
    #       - extra = objeto extra      
    #output - objeto combo
    def crear_combo(self, nombre, platillo, bebida, extra, descripcion) -> object:
        nuevo_combo = Combo(nombre, platillo, bebida, extra, descripcion)
        print(f'La creacion del combos exitosa, se procede a registrarlo')
        self.registrar_combos([nuevo_combo])

class Platillo(Productos):
    def __init__(self, nombre, descripcion, precio):
        super().__init__(nombre, descripcion, precio)
        
    
class Bebida(Productos):
    def __init__(self, nombre, descripcion, precio):
        super().__init__(nombre, descripcion, precio)

class Extra(Productos):
    def __init__(self, nombre, descripcion, precio):
        super().__init__(nombre, descripcion, precio)

class Combo(Productos):
    def __init__(self, nombre, platillo, bebida, extra, descripcion, precio=0):
        super().__init__(nombre, descripcion, precio)
        self.platillo = platillo
        self.bebida = bebida
        self.extra = extra
    
    def calc_precio_combo(self, platillo, bebida, extra) -> int:
        suma = platillo.precio + bebida.precio + extra.precio
        descuento = suma - (suma*.1)
        return descuento 

class Handler(Combo):
    def __init__(self):
        pass

#Ejemplo de uso
handler = Handler()
#Creacion de objetos platillos
campechana = Platillo("campechana", "Platillo rico", 45.50)
tacos_de_trompo = Platillo("tacos de trompo", "Platillo rico", 50.20)
gringas = Platillo("gringas", "Platillo rico", 60.10)
hamburgesas = Platillo("hamburgesas", "Platillo rico", 30.5)
tacos_carne_asada = Platillo("tacos carne asada", "Platillo rico", 45)
sopes = Platillo("sopes", "Platillo rico", 100)
tacos_de_bristec = ("tacos de trompo " ,120)
frijoles_especiales = ("frijoles especiales" , "RICOS",120)
tacos_de_suadero = ("tacos de suadero","RICOS",150)
tacos_de_suadero = ("tacos de suadero","RICOS",180)

#Lista de platillos
platillos = [campechana,gringas]

#Registro de platillos
registro_platillos = handler.registrar_platillos(platillos)

#Creacion de objetos bebidas
refresco = Bebida("refresco", "Bebida rica", 15)
agua = Bebida("agua", "Bebida rica", 18.5)
jugo = Bebida("jugo", "Bebida rica", 22.5)
aguas = Bebida("boing de mango","RICOS", 25)
#Lista de bebidas
bebidas = [refresco, agua, jugo,aguas]

#Registro de bebidas
registro_bebidas = handler.registrar_bebida(bebidas)
df1 = pd.DataFrame(registro_bebidas)
file_write_write = open ("/Users/kapy_10/Big data/Rayados/a.txt")
file_write_write.write  (df1.to_string())
file_write_write.close()
#Creacion de objetos extras
papas_fritas = Extra("papas fritas", "Extra rico", 55)
papas_enchiladas = Extra("papas enchiladas", "Extra rico", 33.5)
ensalada = Extra("ensalada", "Extra rico", 70)

#Lista de extras
extras = [papas_fritas, papas_enchiladas, ensalada]

#Registro extras
registro_extras = handler.registrar_extra(extras)

#Creacion de objetos de Combos
combo_patrio = Combo("combo patrio", enchiladas.nombre, agua.nombre, papas_enchiladas.nombre, "Combo rico", handler.calc_precio_combo(enchiladas, agua, papas_enchiladas))
combo_loco = Combo("combo patrio", flautas.nombre, jugo.nombre, papas_fritas.nombre, "Combo rico", handler.calc_precio_combo(flautas, jugo, papas_fritas))
combo_feliz = Combo("combo patrio", sopes.nombre, refresco.nombre, ensalada.nombre, "Combo rico", handler.calc_precio_combo(sopes, refresco, ensalada))
#Lista de Combos
registro_combos = [combo_patrio, combo_loco, combo_feliz]

#Registro de combos
registro_combos = handler.registrar_combos(registro_combos)

#Creacion de combo


print(registro_platillos)
print(registro_bebidas)
print(registro_extras)
print(registro_combos)




