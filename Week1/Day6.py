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
# one important take is that IN cheks keys not values

# Part 5: Looping over a dictionary:
# we can loop over a dictionary as we did the same in the list. 
# But here we will be returned a key so the loop would be over the key.
given_scores = {"Q1": True, "Q2": False, "Q3": True}
for key in given_scores:
    print(key) # like in the lists it would print the str or an int. 
# but here in the terminal we only get the keys not the value
# but to get the values as well
for g in given_scores:
    print(g, given_scores[g]) # here this would print the key as well as the values.

# but we can use .items() to reach for both- It hands us both key and value.
for k, v in given_scores.items(): # the syntax if we using .items()
    print(k, v)

# Part 5: Concept check:
results = {"Q1": True, "Q2": False}
for k in results:
    print(k)
# 1. This above print statement will only print the keys. Not values
# Rewriting the loop:
for k, v in results.items():
    print(k, v) # here i have used .items to catch both keys and value.

# 3. as suggested in the above line 65 .items will also fetch for values not just keys
# as we did in plain loop.