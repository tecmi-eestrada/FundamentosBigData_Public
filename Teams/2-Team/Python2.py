
#Comida Mexicana: Antojito 
#fecha 1994 de octubre 
#Mascota: Chicharrin 

    
#definición de atrubutos de restaurantes 

fundacion =  1969
def _init_(self, nombre, tipo, fundacion, mascota):
# ---Definicion de atributos
self.identidad = "Tus Antojitos"
self.tipo =  "antojitos mexicanos"
self.fundacion = fundacion
self.mascota = "taquito feliz"


def _str_(self):
    return f"Bienvenido a_{self.identidad} - {self.tipo}, fundado en {self.fundacion}"





