


class Priscila:
    def __init__(self):
        self.nombre = "priscila"
        self.apellido = "garcia"
        self.edad = 18
        self.genero = "femenino"


    def registrar_priscila(self, nombre) -> list:
        output = []
        for nombre in priscila:
            dic_nombre = {
                "priscila": nombre.nombre,
                "garcia": nombre.apellido,
                "18":   nombre.edad,
                "femenino":nombre.genero
            }
            
            output=dic_nombre 
            print(Priscila.registrar_priscila())
        return output

    def datos_priscila(self) -> str:
        return f'''hola soy {self.nombre} mi apellido es {self.apellido} 
                 mi edad es  {self.edad}. 
                     mi genero es {self.genero}!'''
    
priscila=Priscila()
print(priscila.datos_priscila())
           
    
     