class leonel:
    print()
    def __init__(self, nombre, apellido, edad, hobbie, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.hobbie = hobbie
        self.carrera = carrera

    def nombre2(self) -> list:
        output = [{"nombre": self.nombre, "apellido": self.apellido}]
        print(f'Registro de {len(output)} nombre completado con exito')
        return output

    def edad2(self) -> list:
        output = [{"edad": self.edad}]
        print(f'Registro de {len(output)} edad completado con exito')
        return output

    def hobbie2(self) -> list:
        output = [{"hobbie": self.hobbie}]
        print(f'Registro de {len(output)} hobbie completado con exito')
        return output

class nombre(leonel):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido, None, None, None)

    def nombrecompleto(self) -> str:
        return self.nombre + " " + self.apellido

class Edad(leonel):
    def __init__(self, edad):
        super().__init__(None, None, int(edad), None, None)

    def edadcompleto(self) -> int:
        return self.edad 

class Hobbie(leonel):
    def __init__(self, hobbie):
        super().__init__(None, None, None, hobbie, None)

    def hobbiecompleto(self) -> str:
        return self.hobbie



nombre_completoo = nombre("Benito Leonel", "Garcia Castillo")
print(nombre_completoo.nombrecompleto())
print(nombre_completoo.nombre2())
print()

edad_completoo = Edad("18")
print(edad_completoo.edadcompleto())
print(edad_completoo.edad2())
print()

hobbie_completo = Hobbie("tenis de mnesa")
print(hobbie_completo.hobbiecompleto())
print(hobbie_completo.hobbie2())
print()