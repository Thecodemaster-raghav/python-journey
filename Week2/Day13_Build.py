# Build: Pearl Persistence.
# design template:
# we need a class called pearl with some attributes. will then save them in a json file as json type data
# using dump, will use functions like default to make the data serialisable in json and utf-8 for char encoding
# then will load the data back as json.load. thn will have to reconstruct every object as python file 
# so for doing that will have to have another default function working on loaded file.
# in data we need a list of dicts or set inside the class as instance.
import json

class Pearl:
    def __init__(self, topic, fact, difficulty):
        self.topic = topic
        self.fact = fact
        self.difficulty = difficulty

my_data = [
    Pearl("Radiology", "Xrays and MRI", "Hard"),
    Pearl("Anatomy", "Human body", "Easy"),
    Pearl("Cardiology", "Heart", "Medium"),
]

def convert(obj):
    if isinstance(obj, Pearl):
        return obj.__dict__

# initiating a error handling block as sometimes we forget to encode
try:
    with open("mypearls.json", "w", encoding="utf-8") as f:
        json.dump(my_data, f, default=convert, indent=2)
except TypeError:
    print(f"Invalid object name")

with open("mypearls.json", "r", encoding="utf-8") as l:
    load = json.load(l)
    new_data = []
    for i in load:
        my_pearls = Pearl(**i) # this part rebuild dict to object on a round trip
        new_data.append(my_pearls)
# to get all the pearls 
for n in new_data:
    print(n.topic, n.fact, n.difficulty)