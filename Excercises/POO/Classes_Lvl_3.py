#Class definiton

class Store():
    #Constructor definition with default values
    def __init__(self, name = "", brand = "", capacity = 0, displays = 4):
        self.name = name
        self.brand = brand
        self.capacity = capacity
        self.displays = displays
        self.employees = 10
        self.desktops = 10

    def store_data(self):
        print(self.name, self.brand, self.capacity, self.displays, self.employees, self.desktops)

class Telcel(Store):
    def __init__(self):
        Store.__init__(self,"Nuevo Sur", "Telcel", 15, 8)
    
class Template(Store):
    def __init__(self, name="", brand="", capacity=0, displays=4):
        super().__init__(name, brand, capacity, displays)

myStore = Telcel()
myStore.store_data()

myTemplate = Template()
myTemplate.store_data()