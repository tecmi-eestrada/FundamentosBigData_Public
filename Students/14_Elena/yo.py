Platillos=[{
    "Platillo 1:  ":" ENCHILADAS ROJAS ESTILO ZACATECAS","Ingredientes: ":"4 Tacos de lomo de cerdo deshebrado, con una salsa de chile de árbol y chile guajilo","Precio: ":120,
},
{
    "Platillo 2:  ":" EMPANADAS DE CHORIQUESO","Ingredientes: ":"4 Empanadas de queso manchego con chorizo español, acompañadas de salsa macha","Precio: ":120,
    
},
{
    "Platillo 3:  ":" ENMOLADAS CON QUESO","Ingredientes: ":"4 tacos dorados de queso fresco, bañados en una salsa de mole","Precio: ":120,
    
},
{
    "Platillo 4:  ":" MOLOTES DE CHILE RELLENO","Ingredientes: ":"3 chiles guajillos rellenos de queso","Precio: ":120,
},
{
    "Platillo 5:  ":" CHIMICHANGAS DE CHILORIO","Ingredientes: ":"3 chimichangas con reyeno de carne de res en salsa roja","Precio: ":120,
},
{
    "Platillo 6:  ":" CHILAQUILES SALSA VERDE","Ingredientes: ":"200 gr de tortila estilo totopo, bañados en una salsa verde de tomatillo","Precio: ":120,
},
{
    "Platillo 7:  ":" ENCHILADAS SUIZAS","Ingredientes: ":"5 tavos de pollo, bañados en una salsa verde de tomatillo con cilantro","Precio: ":120,
},
{
    "Platillo 8:  ":" GORDITAS DE CARNE","Ingredientes: ":"3 gorditas de maiz rellenas con lomo de cerdo en salsa de chile de arbol","Precio: ":120,
},
{
    "Platillo 9:  ":" EMPALMES ROJOS","Ingredientes: ":"3 empalmes rellenos de carne molida y frijoles con chorizo","Precio: ":120,
},
{
    "Platillo 10:  ":" MOLLETES","Ingredientes: ":"3 mitades de pan lagunero, dorado y embarrado de frijoles con queso y pico de gallo","Precio: ":120,
}]

def imprimirllavevalor(Platillos):
    for llave,valor in Platillos.items():
        print(f"{llave},{valor}")

import pandas as pd
df1=pd.DataFrame(Platillos)

file_to_write=open("c:/Users/Elena Reyes/Desktop/yo.txt", "w")
file_to_write.write(df1.to_string())
file_to_write.close()
