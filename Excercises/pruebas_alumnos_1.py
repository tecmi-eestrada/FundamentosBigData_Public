'''
1. Realizar una lista que contenga:
    3 - string
    2 - integer
    2 - float
    2 - bool
    1 - lista vacia
'''
listatarea = ["tarea1","tarea2","tarea3",3,2,1.1,1.2,True,False,[]]

'''
2. Crear una funcion que reciba una lista e imprima de una en uno su contenido
'''
lista = [1,2,3,4]

def imprimir_lista(funcion_ejemplo):
    for elemento in funcion_ejemplo:
        print (elemento)
        
imprimir_lista(lista)
imprimir_lista(listatarea)

'''
3. Crear un diccionario cuyas llaves sean:
    - nombre
    - apellido
    - edad
    - carrera
    - semestre
y los valores sean su informacion.
'''
diccionario = {
    "nombre" : "Emiliano",
    "apellido" : "Navarro Ramos",
    "edad" : 18,
    "carrera" : "IDS",
    "semestre" : 4,

}
'''
4. Crear una funcion que imprima solo las llaves en una lista
'''
def imprimir_llaves(diccionario):
    for elemento in diccionario.keys():
        print (elemento)

imprimir_llaves(diccionario)
'''
5. Crear una funcion que imprima llave y valor con formato f-string
'''
def imprimirllavevalor(diccionario):
    for llave,valor in diccionario.items():
        print(f"{llave},{valor}")
imprimirllavevalor(diccionario)

'''
6. Crear una funcion que valide el tipo de dato de los elementos de la lista
'''
def validar_lista(listatarea):
    for elemento in listatarea:
        if type(elemento) == str:
            print("El tipo de dato es str")
        elif type(elemento) == int:
            print("El tipo de dato es entero")
        elif type(elemento) == float:
            print("El tipo de dato es flotante (decimal) ")
        elif type(elemento) == bool:
            print("El tipo de dato es booleano")
        elif type(elemento) == list:
            print("El tipo de dato es lista")
        else:
            print("El tipo de dato no es reconocido")

validar_lista(listatarea)

'''
7. Crear una una lista que contenga 10 elementos (de cualquier tipo)
'''
lista = [1,2,3,4]

'''
8. Crear una funcion que añada el contenido de una lista al final de otra
'''
def unir_lista(lista_1, lista_2):
    nueva_lista = lista_1 + lista_2
    print(nueva_lista)

unir_lista(listatarea, lista)

'''
10. Crear una funcion que agregue solicite al usuario 4 datos y que regrese un diccionario
'''

'''
11. Crear una funcion que tome un diccionario y regrese 2 listas (lista_llaves y lista_valores)
'''
def lista_disccionarios (diccionario):
    lista_llaves = diccionario.keys()
    lista_valores = diccionario.values()
    print(lista_llaves)
    print(lista_valores)

lista_disccionarios(diccionario)

'''
12. Crear una funcion que modifique los datos de un diccionario existente y reemplazarlos
'''

'''
13. Crear una funcion que, mientras la longitud de los elementos de una lista sea mayor a 0, imprima cada uno de los elementos
'''

'''
14. Crear una funcion que añada valores al final de una lista en base a un valor entero proporcionado e imprima la lista
'''

'''
15. Crear una funcion que elimine los duplicados de una lista
'''

'''
16. Crear una funcion que convierta en minusculas, mayusculas o la primera en mayuscula y las demas en minuscula en base a un argumento en la funcion
'''