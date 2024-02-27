class Mi_Persona:
    def __init__(self, nombre,apellido, edad, fecha, edad_Actual, arma ):
     self.nombre = nombre
     self.apellido = apellido
     self.edad = edad
     self.fecha = fecha
     self.edad_Actual = edad_Actual
     self.arma = arma
    
    def anecdota(self) -> str:
        return f'''Hola soy {self.nombre} {self.apellido} con {self.edad} el día {self.fecha} fui asaltada en el camion con mis hermanas, 
        dato curioso, ese día cumplia años y al ratero lo sacaron a patadas'''
    
    def miedo(self) -> str:
        return f'''{self.nombre} ahora con {self.edad_Actual} tiene miedo de que la vuelvan a asaltar el {self.fecha}'''
    
    def solucion(self) -> str:
        return f'''Ahora {self.nombre} para solucionar su miedo, lleva siempre {self.arma} a sus {self.edad_Actual} sabe
        que ya no va a volver a suceder'''
    
Lucero= Mi_Persona(" Lucero ","Jaime", 15, " 22 de diciembre", 20, "gas pimienta")

print (Lucero.anecdota())
print (Lucero.miedo())
print (Lucero.solucion())