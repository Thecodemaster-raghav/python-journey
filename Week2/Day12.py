# Day 12 classes and OOPS (by far the most important topic
# so a class is what binds the data and function together
# earlier we did
pear_id = {"id": "P1", "difficulty": "Easy", "times_wrong": 3}

# in this case behavior lives somewhere else and the data is passed in everytime
def mark_wrong(pearl_id):
    pear_id["times_wrong"] += 1
# in this case the mark_wrong and pear_id are strangers who have to be introduced evrytime we call it.

# while in classes we do not need to pass data to a function. THE DATA AND THE THING THAT ACTS ON THE DATA 
# ARE IN one object living inside the class
# class Pearl:
#    def marked_wrong(self):
#        self.times_wrong += 1
# there is a special python method called __int__ which helps us get the starting point for our data
# def __init__ is meant initialize. and the whole job of it is to st up the stating data.
class Pearl:
    def __init__(self, pearl_id, difficulty):
        self.id = pearl_id
        self.difficulty = difficulty
        self.wrong_ans = 0

    def marked_wrong(self):
        self.wrong_ans += 1
p1 = Pearl("p1", "Easy")
p2 = Pearl("p2", "Hard")
p2.marked_wrong()
p1.marked_wrong()
p1.marked_wrong()
print(p2.wrong_ans)
print(p1.wrong_ans) # here we would get 1 as the output as here the self works as wrong_ans
print(p1.difficulty)# here the output would be "Hard" as self was called and 

# made a class for my girlfriend
class Shriyam:
    def __init__(self, beauty, profession):
        self.beautiful = beauty
        self.profession = profession

    def her_age(self):
        self.age = int(input())
        print("Shes incredible")

her_beauty = Shriyam("Out of this world", "Surgeon")
her_beauty.her_age()
print(her_beauty.beautiful)
print(her_beauty.profession)

class Fan:
    def __init__(self, speed, is_on):
        self.speed = speed
        self.is_on = is_on

    def describe(self):
        print(f"The speed  of the fan: {self.speed} and {self.is_on}")

    def turn_off(self):
        self.is_on = False

    def speed_up(self):
        self.speed += 1

bedroom_fan = Fan(3, True)
living_room_fan = Fan(5, False)
office_fan = Fan(7, True)
living_room_fan.speed_up()
living_room_fan.speed_up()
bedroom_fan.turn_off()
office_fan.describe()
bedroom_fan.describe()
living_room_fan.describe()
print(bedroom_fan.speed)
print(living_room_fan.is_on)
print(living_room_fan.speed)

# so self equals to the variable that we use to call the object of the class and multi instance is that we can have as 
# many objects in a class and they all can have separate data and functionalities without mixing them up with
# one and other.
# self is how we refer to the method refers to whichever object is called.

# Concept : object holding and interacing with other objects.
# it means we are adding another layer where objects can hold other objects and methods can call other methods
class Room:
    def __init__(self, name):
        self.name = name
        self.fans = [] # a list that will hold a fan object
    
    def add_fan(self, fan):
        self.fans.append(fan) # here putting fan object into this rooms list.

# Exercise 3 added another method inside the class Room which will reach out to the Fan classmethod
# and will loop over the objects of describe() method.
    def describe_all(self):
        for f in self.fans:
            f.describe()

my_room = Room("Bedroom")

my_room.add_fan(bedroom_fan) # notice here we are making a new object and calling the other object bedroom_fan
my_room.add_fan(office_fan) # same done here calling the other object office_fan and my_room
# so here it holds the whole objects inside not just the attriutes of the objects but the whole thing.
print(my_room.fans[0].speed)
print(my_room.fans[0].is_on)
print(len(my_room.fans))
my_room.describe_all()

# Testing indepenence
study_room = Room("Study")
study_room.add_fan(office_fan)
print(len(study_room.fans)) # here the len will be 1 as only office_fan is added to the object study_room
print(len(my_room.fans)) # remains 2 as there is no changes made in the my_room bject that proves independence


class Players:
    def __init__(self, names, num_players): # class playlist with names and build as attributes and an empty list
        self.names = names
        self.num_players = int(num_players)
        self.teams = []

    def item(self, players): # a method that we use to add the object
        self.teams.append(players)

    def team_players(self):
        total = 0
        for t in self.teams:
            count = t.names
            count_2 = t.num_players # for the players and jersey name to be inside
            print(count, count_2)
            total = total + count_2 # adding to the running total
        return total
    
given_items = Players("ronaldo", 7)
team_sheet = Players("neymar", 10)
given_items.item(given_items)
given_items.item(team_sheet)
print(given_items.team_players())

# inheritance: in inheritance we write one parent class with several child class that
# shares stuff with the child class.
# eg:
class Appliance:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def power_on(self):
        print(f"{self.brand} powering on")

# then the child class that inherits from it and gets all of that for free adds its own.
class Fridge(Appliance): # here fridge is the inherited class and Appliance is the parent class
    
    def __init__(self, brand, price, has_water):
        super().__init__(brand, price)
        self.has_water = bool(has_water)
    
    def making_ice(self):
        print(f"{self.brand} makes ice")


class Washer(Appliance):
    def __init__(self, brand, price, capacity):
        super().__init__(brand, price)
        self.capacity = float(capacity)

    def what_capacity(self):
        print(f"{self.brand} has {self.capacity}")


my_fridge = Fridge("LG", 1800, True)
my_washer = Washer("Samsung", 1900, 5.0)
my_fridge.making_ice()
my_washer.what_capacity()