#ORIENTADO_A_OBJETOS

class Restaurante:
    def __init__(self, nombre, tipo_comida, Año_fundacion, mascota):
        self.nombre = nombre 
        self.TipoComida = tipo_comida
        self.fundacion = Año_fundacion
        self.mascota = mascota



NuestroObjeto = Restaurante("PollitoAnabolico", "Oriental", 2002, "Mapache")

print(NuestroObjeto.nombre)
print(NuestroObjeto.TipoComida)



