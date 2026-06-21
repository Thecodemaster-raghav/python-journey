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
        print(loaded_file)
except json.JSONDecodeError:
    print(f"Data is not appropriate, file in not valid JSON format")

# deserialization from json -> python that is known as deserialization
# Edge cases - Set, tuple and dicts 
notes = {"raghav", "shubham", "karan", "happy"}
# note = json.dumps(notes)
# print(note) # we saw here it error outs as set is not json serializable 
# json does not have a close data type conversion for a set so it hands back a error.
# while in a tuple a close one to the list in python when we dump the data into json it turns
# it to json array and when loaded back to python it loads it as a list.
small_dict = {1: "a", 2: "b"}
cool = json.dumps(small_dict)
print(cool) # a thing to notice here is that the keys of a dicts are changed to a string the values stays untouched.
# like in small_dict 1 turns to "1" on the round trip becuase JSON object keys must be string.

new_dict = {"Topic": "Anatomy", "year": 2026, "was_correct": True, "note": None}
location = (4, 112)
attempts = {1: "misses", 2: "right ans"}
tags = ["anatomy", "radiology", "nephrologist"] # converted set into a list

# when we dump the new_dict just the "was_correct" and "note" is changed to true and null all the other stays the same 
# which is a string
# location becomes a array
# in attemots the keys are changed to strings because JSON object keys must be a string.
# tags will give an error

print(json.dumps(new_dict))
print(json.dumps(location))
print(json.dumps(attempts))
print(json.dumps(tags))

loaded_dict = json.dumps(new_dict)
result = json.loads(loaded_dict)
print(result)

# key takeaway is that the json.dumps needs to work with json.loads it works as a pair not separate.

# Part 1 and 2 exercises: the nested session record

session = {
    "SUBJECT": "RAG", "Scores": (205, 405, 605), "coords": (2,5), 
    "minutes":{1: "warmup", 30: "MCQS"},
    "Topics": ["raghav", "shubham", "ronaldo", "messi"],
    "done": True, "none": None
           }
my_session = json.dumps(session)
print(my_session) # here we are getting an error because we have a set in the data ans json cannot serialize it.
# now that we have changed the set to a list the data will be serialized by json. A string for keys of dict a
# list or array of scors and coords

# now the round trip: json.loads
load_session = json.loads(my_session)
print(load_session)

# Exercise 2: writing a json string by hand
shape = '{"id": "P1", "marks": 25, "correct": true, "explaination": null, "options": ["raghav", "keshav", "sahib"],"meta": {"subject": "anatomy"}}'
shape_loaded = json.loads(shape)
print(shape_loaded)

# Part 3: Output control
# this means we change the look of the serialised output of json.dumps
# there are 3 rungs: Indent, sort_keys, ensure_ascii

# checking indent:
sessions = {
    "SUBJECT": "RAG", "Scores": (205, 405, 605), "coords": (2,5), 
    "minutes":{1: "warmup", 30: "MCQS"},
    "Topics": ["raghav", "shubham", "ronaldo", "messi"],
    "done": True, "none": None
           }

my_sessions = json.dumps(sessions, indent=2) # it is just the cosmetics. pretty printing it for the users 
# print(my_sessions) # indenting means 

# now sort_keys this means that dumps write evrything in the alphabatical order every time when put in inside json.dumps

# why do we do that? to make equal data look equa to any comparable bytes.

my_sorted = json.dumps(sessions, indent=2, sort_keys = True)
# print(my_sorted) # so that same keys comes out as alphabetical order

names = {"name": "राघव"}
my_name = json.dumps(names)
my_names = json.dumps(names, ensure_ascii = False) # to ensure that we do not have values coming out as ascii codes
# when something is not typed in english. The reason to set this false is readability.
print(my_name)
print(my_names)

data = {"Zebra": 1, "apple": 2, "Mango": 3, "banana": 4}
my_data = json.dumps(data, sort_keys= True)
print(my_data) # prints everythng alphabetical order but the alphabets in uppercase holds higher value in asci characters.

# exercise : indent and nesting depth
data2 = {"user": "raghav", "scores": [91, 85], "meta": {"city": "Saskatoon"}}
my_data2 = json.dumps(data2, indent = 4)
print(my_data2) # here we will have 8 spaces sitiing infront of city: Saskatoon

# exercise 3: combine all three
new_data = {"City": "Montreal", "name": "राघव"}
my_new_data = json.dumps(new_data, indent=2, ensure_ascii=False) # because ensure_ascii is always true
print(my_new_data)