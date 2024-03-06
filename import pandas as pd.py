import pandas as pd

class Bar:
    def __init__(self, nombre, tipo_de_bar, fundacion):
        self.nombre = nombre
        self.tipo = tipo_de_bar
        self.ano_de_fundacion = fundacion

    def datos_bar(self) -> str:
        return f'''Bienvenidos a {self.nombre}, un bar especializado en {self.tipo} 
                con una tradición desde {self.ano_de_fundacion}.'''

class Producto:
    def __init__(self, nombre, descripcion, precio:float):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

    def registrar_producto(self, productos) -> list:
        output = []
        for producto in productos:
            dic_producto = {
                "nombre": producto.nombre,
                "descripcion": producto.descripcion,
                "precio": producto.precio
            }
            output.append(dic_producto)
        print(f'Registro de {len(productos)} productos al menú fue exitoso')
        return output

class BebidaAlcoholica(Producto):
    def __init__(self, nombre, descripcion, precio, origen, grado_alcohol):
        super().__init__(nombre, descripcion, precio)
        self.origen = origen
        self.grado_alcohol = grado_alcohol

# Ejemplo de uso
# Creación de objetos de bebidas alcohólicas
whisky = BebidaAlcoholica("Whisky", "Bebida de alta graduación", 120, "Escocia", "40%")
vodka = BebidaAlcoholica("Vodka", "Destilado popular", 80, "Rusia", "40%")
tequila = BebidaAlcoholica("Tequila", "Destilado de agave", 90, "México", "38%")

# Lista de bebidas alcohólicas
bebidas_alcoholicas = [whisky, vodka, tequila]

# Registro de bebidas alcohólicas
registro_bebidas = Producto("Bebidas Alcohólicas", "", 0)
registro_bebidas_alcoholicas = registro_bebidas.registrar_producto(bebidas_alcoholicas)

# Crear DataFrame y guardarlo en un archivo .txt
df_bebidas = pd.DataFrame(registro_bebidas_alcoholicas)
file_path = "C:\Users\Rober\OneDrive\Documentos\4to semestre tecmi tareas\import pandas as pd.py/a.txt"
with open(file_path, "w") as file:
    file.write(df_bebidas.to_string())

print(registro_bebidas_alcoholicas)
