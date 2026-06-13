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