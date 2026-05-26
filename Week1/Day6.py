# Day 6 of dictionaries:
# part 1 what are dictionaries: So like as we did in the qUIZ TRACKER THAT WE did not had any link between the lists
# but instead we formed it using indexing day 2 concept.
# But in a dictionary makes that link explicit. 
# key value pair are stored inside of a DICTIONARY where a key directly point towards its value.
# example:
fifa_brazil = {"NEYMAR JR": True, "Cristiano": False}
# so here i have done in the example 
# "CRISTIANO "is the key and it points to a vlaue which is false
# curly brases are used to represent the dictionary
person = {"name": "Raghav", "day": 6} # Here person is found by a key.

# so for that we put the key inside a square brackets and then then call it,
print(person["name"])

student = {"name": "Shriyam", "day": 6, "passed": True}
print(student["passed"])# here we are calling studen with the key "passed" and the value againts it gets printed.
print(student["name"]) # here we are calling the student using key "name" and the value againets the key gets printed.
 # print(student[day]) # just to check what happens and in this case python thinks of it as a VARIABLE 
# not a key inside student.

# Part 3 is adding and updating:
# syntax - dict[key] = value - so this means if lets say you want to add a value inside of a list.
# we will use this syntax even if we want to update it.
student["day"] = 7 # updating the value of the "day" key.
student["doctor"] = True # here adding the value and a key to the dictionary.

# quick exercise
data = {"a": 1}
data["a"] = 5 # the values gets updated to 5 since the key already exists inside the dictionary
data["b"] = 9 # this gets added to the dictionary and a new key value pair is creating.
# as python sees nothing inside "b" = 9. so it creates a new key value pair.

# Part 4: checking is the key exits.
# here we check for the missing key crashes.
# The in Keyword helps in checking the key "asking is this key in the dictionary"
# and gives back True or False
club_eng = {"manunited": True, "real madrid": False}
print("score" in club_eng)
print("real madrid" in club_eng)