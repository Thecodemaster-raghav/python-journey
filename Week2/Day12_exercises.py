# day 12 inheritance
# if we call my_washer.power_on and we have already overriden the power_on methods inside of the
# the child class fridge than the versionof the child class runs as python checks inside the child class
# first and than moves onto the parents version but since it is overriden only the child class version runs 

# Exercise 1: washer not overrriden
from Day12 import Appliance, Fridge, Washer

my_washer = Washer("Bosch", 1800, 7.5)
my_washer2 = Fridge("LG", 1900, 2.0)
my_washer.power_on() # here i have added the power_on method inside of the washer class and then called super 
# that is why it prints 2 lines firstly the parent class method then Washer's own power_on method
my_washer2.making_ice() 

class Dryer(Appliance):

    def __init__(self, brand, price, heat_level, vented):
        super().__init__(brand, price)
        self.heat_level = str(heat_level)
        self.vented = vented

    def start_drying(self):
        print(f"{self.brand} will dry at {self.heat_level}")

my_dryer = Dryer("Samsung", 1900, "55degrees", True)
my_dryer.power_on()
my_dryer.start_drying()

# cumulative inheritance exercise: building a inventory manager from scratch for a appliance store
# building a store class and this is a individual class it will not inherit 
# store class will work as a container- HAS/A learning that we used.

class Store:
    def __init__(self, name):
        self.name = name
        self.inventory = []
# here we will be appending the object to the list
    def add_appliance(self, appliance):
        self.inventory.append(appliance)

    def total_value(self):
        total = 0 # but this only stays outside for the whole value to store
        for s in self.inventory:
            total = total + s.price
        return total
    
    def power_on_all(self):
        for i in self.inventory:
            i.power_on()

my_store = Store("Indian Appliances")
my_fridges = Fridge("LG", 1800, True)
my_washers = Washer("Bosch", 2200, 7.4)
my_dryers = Dryer("Samsung", 2400, "68 degrees", False)
my_store.add_appliance(my_fridges)
my_store.add_appliance(my_washers)
my_store.add_appliance(my_dryers)    
my_store.power_on_all()
print(f"Total package price: {my_store.total_value()}")