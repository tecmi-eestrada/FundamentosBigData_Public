'''
-Registrar Extras en el menu (deberan tener minimo 8 extras)
    -Cada Extra debe contar con:
        -Nombre del extra
        -Descripcion (ingredientes y cantidad)
        -Precio
'''
print()
lista_Extras_Nombre =      ["Ketchup", "Mayonesa", "Mostaza", "Ranch", "Queso", "Salsa verde", "Salsa roja", "bbq"]
lista_Extras_Descripcion = ["sobre de salsa de tomate", "sobre de mayonesa", "sobre de mostaza", "sobre de ranch", "150g de queso amarillo para papas a la francesa", "sobre de salsa verde", "sobre de salsa roja", "sobre de  bbq"]
lista_Extras_Precio=       ["$5", "$5", "$5", "$25", "$20", "$15", "$18", "$25",]



def imprimir_elementos_nombre(lista_Extras_Nombre):

    for elemento in lista_Extras_Nombre:
        print(elemento)

def imprimir_elementos_descripcion(lista_Extras_Descripcion):

    for elemento in lista_Extras_Descripcion:
        print(elemento)

def imprimir_elementos_precio(lista_Extras_Precio):

    for elemento in lista_Extras_Precio:
        print(elemento)

imprimir_elementos_nombre(lista_Extras_Nombre)
print()
imprimir_elementos_descripcion(lista_Extras_Descripcion)
print()
imprimir_elementos_precio(lista_Extras_Precio)
    