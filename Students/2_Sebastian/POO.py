class Sebastian:
    def __init__(self, Nombre, edad, color_piel, sexo, hobbie, inLove, nombre, juegos, carrera):
        self.nombre = Nombre
        self.edad = edad
        self.color_piel = color_piel
        self.sexo = sexo
        self.hobbie = hobbie
        self.inlove = inLove
        self.Nombre = nombre
        self.juegos = juegos
        self.carrera = carrera

    def presentacion(self):
        return f''' HOLA, mi nombre es {self.nombre}, tengo {self.edad}, me considero con un 
        color de piel {self.color_piel}, soy de genero {self.sexo}, y me gusta mucho {self.hobbie}'''
    
    def fallinInLove(self):
        return f''' Hola soy yo de nuevo {self.nombre}, pero ahora quiero hablar sobre mi {self.inlove},
        soy muy feliz al lado de ella y es la primera mujer en la que confio, y su nombre es {self.Nombre}'''
    
    def Pasado(self):
        return f''' Lamentablemente perdi mucho tiempo en los {self.juegos}, y no logre aprender y disfrutar de muchas
        cosas a temprana edad extraño mucho esos tiempos :('''
    
    def Educacion_Actual(self):
        return f''' Actualmente me encuentro estudiando la carrera de {self.carrera}, y me encuentro en el punto
        de mi vida en el cual no se si irme por Bases de datos o CyberSecurity'''
    
datos = Sebastian("Sebastian", 18, "moreno", "Masculino", "CORRER", "relacion amorosa", "Nhylze", "VideoJuegos", "IDS")
print("BUENOS DIAS, BUENAS TARDES, BUENAS NOCHES")
print(datos.presentacion())
print(" ") 
print(datos.fallinInLove())
print(" ")
print(datos.Pasado())
print(" ")
print(datos.Educacion_Actual())
  
    




    
        


    
  



    