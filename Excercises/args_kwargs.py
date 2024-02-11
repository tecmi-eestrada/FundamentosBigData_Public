# args, *args, **kwargs
# single asterisk (*) to unpack iterables
# two asterisks (**) to unpack dictionaries

#----------------------------------------------------------------------
#Funcion que suma todos los elementos de una lista
def sumatoria(num_enteros):
    resultado = 0
    for numero in num_enteros:
        resultado += numero
    return resultado

#Creacion de lista con elementos enteros
list_de_enteros = [1, 2, 3]

#Impresion de resultado
# print(sumatoria(list_de_enteros))
#----------------------------------------------------------------------

def sumatoria_con_args(*args):
    resultado = 0
    # Iterating over the Python args tuple
    for numero in args:
        resultado += numero
    return resultado

# print(sumatoria_con_args(1, 2, 3))
#----------------------------------------------------------------------

def concatenar_datos(**kwargs):
    resultado = ""
    # Iterating over the Python kwargs dictionary
    for arg in kwargs.values():
        resultado += arg
    return resultado

def concatenar(**kwargs):
    resultado = ""
    # Iterating over the Python kwargs dictionary
    for key, value in kwargs.items():
        print(f"{key} => {value}")
    return resultado

# print(concatenar_datos(nombre="Erick", apellido="Estrada", edad="31"))
# concatenar(nombre="Erick", apellido="Estrada", edad="31")

var = 32.2
if type(var) == float:
    print(var)