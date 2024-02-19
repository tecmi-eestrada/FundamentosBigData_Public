#----Clase y Objeto en su forma mas simple
#---Definicion de clase
class MiPrimerClase:
    #---Defincion de atributos
    saludo = "Hola, soy la primer clase"

#---Instanciacion de clase; creacion de objeto
mi_primer_objeto = MiPrimerClase()

#---Acceder a los atributos de la clase
print(mi_primer_objeto.saludo)

# ----Definicion de clase
class Restaurante:
    # ---Funcion que inicializa su instanciacion con una estructura definida (tambien llamada constructor)
    def __init__(self, nombre, tipo_de_restaurante):
        # ---Definicion de atributos
        self.identidad = nombre
        self.tipo = tipo_de_restaurante
    
    # ---Funcion que retorna la instancia con una cadena de texto predeterminada
    def __str__(self):
        return f"Bienvenidos a {self.identidad} - {self.tipo}"
    
    # ---Metodo que retorna el menu del restaurante
    def entrega_de_menu(self):
        menu = """
            Bienvenidos a {self.identidad}
                    Menu
                    Hamburguesa sencilla----$50
                    Hamburguesa doble-------$100
             """
        return menu

        
    
#---Defincion de Objeto
# restaurante_hamburguesas = Restaurante("Hamburguecito", "Restaurante Familiar")

#---Impresion de atributos a traves de instanciar el objeto
# print(restaurante_hamburguesas.identidad)
# print(restaurante_hamburguesas.tipo)

#---Modificar los atributos
# restaurante_hamburguesas.identidad = "Deliciosas Hamburguesas"
# print(restaurante_hamburguesas.identidad)
# print(restaurante_hamburguesas.tipo)

#---Impresion de instancia con y sin funcion __str__
# print(restaurante_hamburguesas)

#---Llamada del metodo del objeto
# print(restaurante_hamburguesas.entrega_de_menu())
