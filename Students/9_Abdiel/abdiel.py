class Abdiel:
    def __init__(self):
        self.nombre = "Abdiel" 
        self.apellido = "Hernandez"
        self.edad = 20
        self.genero = "Masculino"
        self.hobbie = "futbol"

    def registrar_abdiel(self, nombre) -> list:
        output = []
        for abdiel in abdiel:
            dic_abdiel = {
                "abdiel": nombre.nombre,
                "hernandez": nombre.apellido,
                "20": nombre.edad,
                "masculino": nombre.genero,
                "futbol": nombre.hobbie,
            }

            out=dic_nombre

        return output

    def datos_Abdiel(self) -> str:
        return f'''Hola soy {self.nombre} el apellido {self.apellido} 
                mi edad es {self.edad}. 
                mi genero es {self.genero}!
                mi hobbie es {self.hobbie}'''


abdiel=Abdiel()
print(abdiel.datos_Abdiel())