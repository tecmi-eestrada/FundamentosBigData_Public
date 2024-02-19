#1. Realizar una funcion que procese una lista y le sume a cada uno el valor de 8
listita = [1,2,3]
listota = [5,6,7]
numero = 3
letra = "A"
def TestFunction1(listOne):
    for i in listOne: 
        suma = i + 8
        print(suma)

TestFunction1(listita)

#2. Crear un diccionario que contenga 10 elementos con valores boolean, int, float, string, list
myFirstDictionary = {
        1:"John", 
        2:7, 
        3:"12/09/2001", 
        4: 65.20, 
        5:True, 
        6:["hormiga", "perro", "elefante"], 
        7:"Trebol", 7:77.75, 
        9:["Lechuga", False], 
        10:{"Z": "Fin", "A":"Inicio"}
    }

#3. Crear una clase con metodos, la clase se llamara OperacionesMatematicas, los metodos recibiran 2 valores enteros
#   los metodos seran suma, resta, division, multiplicacion, exponente cuadrado, y un metodo de impresion
class OperacionesMatematicas():
    def __init__(self,primer_variable, segunda_variable):
        self.l = primer_variable
        self.i = segunda_variable
    
    def suma(self):
        return self.l + self.i

    def resta(self):
        return self.l - self.i

    def division(self):
        return self.l / self.i

    def multiplicacion(self):
        return self.l * self.i

    def exponenteCuadrado(self):
        return self.l ** self.i
    
    @classmethod
    def impresion(self, text, impre):
        print(text, impre)

operacion = OperacionesMatematicas(3,6)
imp = OperacionesMatematicas
imp.impresion("El resultado de la suma es: ",operacion.suma())
# operacion.impresion("El resultado de la suma es: ",operacion.suma())
# operacion.impresion("El resultado de la resta es: ",operacion.resta())
# operacion.impresion("El resultado de la division es: ",operacion.division())
# operacion.impresion("El resultado de la multiplicacio es: ",operacion.multiplicacion())
# operacion.impresion("El resultado del exponente al cuadrado es: ",operacion.exponenteCuadrado())