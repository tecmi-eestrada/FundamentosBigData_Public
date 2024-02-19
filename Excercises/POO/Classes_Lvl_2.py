
class Building():
    #public
    number = 5460
    #protected
    _number2 = 5555
    #private
    __number3 = 1234

    def __init__(self, windows, doors, size):
        self.window = windows
        self.doors = doors
        self.size = size

    # @property
    # def number(self):
    #     return self.number
        
    @number.setter
    def set_new_number(self, new_number):
        self.number = new_number
        
    def builded(self, building):
        print("My Building {} it's done!".format(building))
    
    def home(self):
        print("My Building has {} windows, {} doors and is {} size.".format(self.window, self.doors, self.size))


class House(Building):
    def __init__(self, windows, doors, size):
        super().__init__(windows, doors, size)
    
    def home(self):
        print("My Home has {} windows, {} doors and is {} size.".format(self.window, self.doors, self.size))



building = Building(6,2,"Medium")
# building.builded("Mall")
# building.home()
print(building.number)
print(building._number2)
print(building._Building__number3)
house = House(4,1,"Small")
# house.builded("Home")
# house.home()
# print(house.number)
# print(house.__number3)
# print(building._number2)