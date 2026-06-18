# Day 13 JSON: reading parsing and writing
# why and what is JSON: well  is file format that we use to store data as text.
# why JSON would be because it is the API language.
# JSON looks exactly like that of the python dictionary data structure.
text = {"id": "p1", "difficulty": "Hard"} # -> this is python dictionary format

# now JSON as Text format as we discussed above.
# the mental model: turning dict into JSON text to save it and then turning JSON text back
# into a dict to use it.
# we would need the bult in  module first
import json
pearl = {"id": "p1", "difficulty": "Easy", "was_correct": False} # to notice the difference the JSON will convert the uppercase
# False into a lowercase false for us to notice the difference.
name = json.dumps(pearl) # this is the syntax and this will convert the dict into a JSON string 
print(name) # and here it gets printed
# print(type(name)) # to check what is the data type
# print(type(pearl)) # here it will show dict and the upper version is converted to a string as 
# JSON converts the file to a JSON string.

# now we have converted the pyhton text to JSON now we will convert JSON text back to a python dict
back_to_dict = json.loads(name) # here we use loads method which converts the data back to dict
print(back_to_dict)
# print(type(back_to_dict)) # notable difference that the dict has '' and the JSON has ""

# json.dump and json.load -> the file versions
# json.dump is used to write the python object into a file in json
# json.load is used to read json file back into a python object.

# dump and load needs a file object to work with,  and with open() gived us that.
# json.dump -> writing mode

with open("pearl_data.json", "w") as p:
    json.dump(pearl, p) # here pearl is the object and p is what we are naming our file to use here.

# json.load -> reading mode

with open("pearl_data.json", "r") as f:
    load = json.load(f)

print(load)
print(type(load)) # so in the reading of the file using json.load we read the file back to us as a dict

pearls = [
    {"id": "p1", "difficulty": "Hard", "was_correct": False},
    {"id": "p2", "difficulty": "Easy", "was_correct": True},
    {"id": "p3", "difficulty": "Good", "was_correct": False}
]

# firstly we will be using json.load as we a json file than we will write json.load to load it back or 
# reading mode to make a python dict and then will print all the data and we will use "w" -> write
# "r" as reading file.
# and yes json file holds all three as a list.

with open("pearls_extended.json", "w") as e:
    json.dump(pearls, e)
# now reading the file. using json.load back into the terminal
with open("pearls_extended.json", "r") as l:
    loads_back = json.load(l)

print(loads_back) # printing the file back to the terminal
print(type(loads_back)) # checking the data type of the file

# error-handling a json file:
try:
    with open("broken.json", "r") as file:
        loaded_file = json.load(file)
except json.JSONDecodeError as e:
    print(f"Data is not appropriate: {e}")
    