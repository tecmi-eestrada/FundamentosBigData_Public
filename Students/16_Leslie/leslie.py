class Leslie:
    def __init__(self, nombre, edad, estatura, tez, nacionalidad, cocinar, música, Ejercicio):
        self.nombre = nombre 
        self.edad = edad
        self.estatura = estatura
        self.tez = tez
        self.nacionalidad = nacionalidad
        self.cocinar = cocinar
        self.música = música
        self.Ejercicio= Ejercicio 

    def datos_de_Les (self) -> str:
        return f'''Hola mi nombre es {self.nombre} tengo {self.edad} años de edad, mido {self.estatura}, equivalente a 3 subways, mi tez es {self.tez} y soy {self.nacionalidad}'''

    def Hobbys (self) -> str:
        return f'''Uno de mis hobbys favoritos es {self.cocinar}, disfruto coompartirlo con mis seres queridos.'''

    def Música (self) -> str:
        return f'''Disfruto escuchar  {self.música}, no podría vivir un solo día sin escucharla.'''

    def Actividad (self) -> str:
        return f'''Para sentirme plena conmigo misma, me gusta hacer {self.Ejercicio}.'''


leslie=Leslie("Leslie Elizabeth Vivero Gonzalez", 20, "1.50", "blanca", "Méxicana", "cocinar", "música", "ejercicio")
print(leslie.datos_de_Les())
print(leslie.Hobbys())
print(leslie.Música())
print(leslie.Actividad())