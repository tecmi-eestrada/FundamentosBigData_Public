class Formulas():
    def suma(a,b):
        result = a+b
        return result
    
    def resta(a,b):
        result = a-b
        return result

def funcion():
    pass

a = Formulas()

# print(Formulas.suma(1,18))
# print(a.suma(1,18))

class Humano():
    def __init__(self, name, age, country, phrase):
        self.name = name
        self.age = age
        self.country = country
        self.phrase = phrase
    
    def introduction(self):
        print("Hi, my name is {} and I'm {} years old".format(self.name, self.age))

    def favorite_phrase(self):
        print(self.phrase)
    
    def nationality(self):
        print("I'm from {}".format(self.country))

class Empleado(Humano):
    def __init__(self, name, age, country, phrase, role):
        super().__init__(name, age, country, phrase)
        self.role = role

    def role(self):
        print("Hi, I'm working as a {}".format(self.role))
    
    def full_presentation(self):
        print("Hi, my name is {} and I'm {} years old, I'm from {} working as a {}.".format(self.name, self.age, self.country, self.role))

    def favorite_phrase(self):
        return super().favorite_phrase()

empleado = Empleado("Juan", 26, "Mexico", "Yiiija", "Ingeniero")

empleado.full_presentation()
empleado.favorite_phrase()