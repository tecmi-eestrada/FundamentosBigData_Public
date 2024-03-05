import pandas as pd

bebida1 = [{
    "nombre" : "agua de sabor",
    "ingredientes" : "frutas y agua", 
    "precio" : 35
},
{
    "nombre" : "refresco",
    "ingredientes" : "de sabor o cocacola", 
    "precio" : 25
},

{
    "nombre" : "agua simple",
    "ingredientes" : "agua embotellada", 
    "precio" : 30
},

{
    "nombre" : "limonada mineral",
    "ingredientes" : "limones, endulzante y agua", 
    "precio" : 35
}]

bebidas = pd.DataFrame(bebida1)

import os 
file = open("Menu.txt","w")
file.write(bebidas.to_string())
file.close()

extra1 = {
    "nombre" : "papas a la francesa",
    "descripción" : "papa, sal y especias", 
    "precio" : 40
}

extra2 = {
    "nombre" : "pay de queso",
    "descripción" : "queso crema, lechera, galleta y mantequilla", 
    "precio" : 45
}

extra3 = {
    "nombre" : "coctel de frutas",
    "descripción" : "papaya, piña, manzana y yogurt", 
    "precio" : 35
}

extra4 = {
    "nombre" : "totopos",
    "descripción" : "tortilla frita con dos salsas de la casa", 
    "precio" : 35
}

extra5 = {
    "nombre" : "agua de sabor",
    "descripción" : "frutas y agua", 
    "precio" : 35
}

extra6 = {
    "nombre" : "agua de sabor",
    "descripción" : "frutas y agua", 
    "precio" : 35
}

extra7 = {
    "nombre" : "agua de sabor",
    "descripción" : "frutas y agua", 
    "precio" : 35
}

extra8 = {
    "nombre" : "agua de sabor",
    "descripción" : "frutas y agua", 
    "precio" : 35
}
