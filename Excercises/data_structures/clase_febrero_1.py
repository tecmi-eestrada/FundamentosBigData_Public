import random

PI = 3.141592
EULER = 2.02

#Lista referente a edos de la republica
estados_mexico = ["Aguascalientes", "Baja California", "Baja California Sur", 
                  "Campeche", "Coahuila", "Colima", "Chiapas", "Chihuahua", 
                  "Durango", "CDMX", "Guanajuato", "Guerrero", "Hidalgo", 
                  "Jalisco", "México", "Michoacán", "Morelos", "Nayarit", 
                  "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo", 
                  "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", 
                  "Tlaxcala", "Veracruz", "Yucatán", "Zacatecas"]

# for i in range(len(estados_mexico)):
#     print(estados_mexico[i])

# for contador, estado in enumerate(estados_mexico):
#     if contador == 4:
#         break
#     print(contador, estado)

# is_anotherState = True
# is_goodResponse = True

# #Validacion de estados utilizando While e IF, ELIF y ELSE
# while is_anotherState == True:

#     if is_goodResponse == True:
#         print(random.choice(estados_mexico))

#     print("Para responder SI escribe Y, para responder NO escribe N")
#     my_answer = str(input("Quieres obtener otro estado aleatoriamente? ")).lower()

#     if my_answer == "n":
#         is_anotherState = False
#     elif my_answer == "y":
#         is_anotherState = True
#         is_goodResponse = True
#     else:
#         print("Por favor responde acorde a las instrucciones")
#         is_goodResponse = False

#Creacion de Diccionario
# alumnos = {
#     [
#     "nombre": "Luis",
#     "edad": 23,
#     "carrera": "IDS"
#     ],
    
# }
edos_mexico = {
    "AGU": "Aguascalientes", 
    "BCN": "Baja California", 
    "BCS": "Baja California Sur", 
    "CAM": "Campeche", 
    "COA": "Coahuila", 
    "COL":"Colima", 
    "CHP": "Chiapas",
    "CHH": "Chihuahua", 
    "DUR": "Durango", 
    "CMX": "CDMX",
    "GUA": "Guanajuato",
    "GRO": "Guerrero",
    "HID": "Hidalgo", 
    "JAL": "Jalisco", 
    "MEX": "México",
    "MIC": "Michoacán",
    "MOR": "Morelos",
    "NAY": "Nayarit", 
    "NLE": "Nuevo León", 
    "OAX": "Oaxaca", 
    "PUE": "Puebla", 
    "QUE": "Querétaro",
    "ROO": "Quintana Roo", 
    "SLP": "San Luis Potosí", 
    "SIN": "Sinaloa", 
    "SON": "Sonora", 
    "TAB": "Tabasco", 
    "TAM": "Tamaulipas", 
    "TLA": "Tlaxcala", 
    "VER": "Veracruz", 
    "YUC": "Yucatán", 
    "ZAC":"Zacatecas"
}

# Iterar diccionario con un for
# print(edos_mexico.values())
# for key, value in edos_mexico.items():
#     print(f"La llave es: {key}, el valor es: {value}")


todos_los_estados = []
todos_los_estados.extend(estados_mexico)
todos_los_estados.extend(edos_mexico.values())
# todos_los_estados.sort()
my_set = tuple(todos_los_estados)
print(my_set)