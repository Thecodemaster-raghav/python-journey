# now we are starting off with decorators 
# decorators are the door to FASTAPI

# Functions are objects that we can pass around:
# here we can pass the functions around without calling them using them as values

def greet():
    return "Hello ji"

result = greet
print(result())

def call_it(func):
    return func()

data = call_it(greet)
print(data)

# rep 1: assign and call later
def shout():
    return "HEY"

x = shout
y = x
print(y) # this statement gives us the how the function is saved in python memory
print(y()) # this prints the function cleanly.

# function in a list.
def a():
    return "first"

def b():
    return "second"
func = [a, b]
print(func[1]()) # same as we do in indexes it will locate the indicies inside of the list but same as the above pattern

def bye():
    return "goodbye"

greeting = call_it(bye)
print(greeting)

# nested functions or when a function return a function
def outer():
    def inner():
        return "Raghav is learning decorators and accomplish his dreams"
    return inner # here the nested function rule meaning when we call the outer() func it will return what it is being passed on.

nest_func = outer()
print(nest_func())
print(outer()())

# the returned function still works later
def make_greeting():
    def greet():
        return "namaste"
    return greet
saved = make_greeting()
print(type(saved))
print(saved())

# outer takes an argument hat inner uses:
def multiply(n):
    def time(x):
        return x*n
    return time
double = multiply(2)
total = double(5)
print(total)

# Part 3: adding a behaviour arund a function and then wrapping it. DECORATOR
def totals(num):
# a decorator wraps the function as an extra behaviral element and hands back a wrapped version
    def wrap_total():
        print("How are you")
        results = num() # this is the moment where the wrapped up originals gets executed
        print("done")
        return result # because no return passes a none
    return wrap_total

def get_total():
    print("there is no total")

task = totals(get_total)
print(task()) # a function with no return statement hands back none.

# the "@" swap: 
@totals
def my_total():
    print("Manifestation works")

my_total()

# a decorator in python is just an automatic reassignment
# the @ secretly runs my_total = totals(my_total)

# reps to solidify
def announce(obj):
    def wrapper():
        print("ENGINE START")
        given_func = obj()
        print("CYCLE ENDs")
        return given_func
    return wrapper

def func_a():
    print("doing reps")

funcs = announce(func_a)
funcs() # the manual way

# using @
@announce
def func_b():
    print("still doing reps")

func_b()
print(func_b) # this will show something as the python storing and of what type it is. like a function and some numbers
# pointing at the data storage in python

def order(middle):
    def extra():
        print("[")
        value = middle()
        print("]")
        return value
    return extra

@order
def extra_func():
    print("i will work hard and get a job in big 2027")

extra_func() # here the print 1 works with [ and then the extra_func which i introduced in the middle and then after that ]

# two functions and 1 decorator
@announce
def second():
    print("to show that the decorators can be used in 2 places not just one")

func_b()
second()

import json
# rep 1 : roud trip with a lossy type
dta = {"user": "raghav", "scores": (90, 85), "tag": {"py", "sql"}}

def conversion(obj):
    if isinstance(obj, set):
        return list(dta["tag"])
    
saving_dta = json.dumps(dta, indent=2, default=conversion)
load_dta = json.loads(saving_dta)
print(load_dta) # tuple converts silently on its own, default func for the tag as it is a set

# rep:2 write to a file, modify, re-save

filename = {"user_email": "raghav.s@gmail.com", "user_form": "JEE MAINS"}
def saving(filename):
    with open("rep2.json", "w") as f:
        json.dump(filename, f, indent=2)
saving(filename)

def load():
    with open("rep2.json", "r") as p:
        loaded = json.load(p)
        loaded["filled_form"] = True
        return loaded
load()

def data_back(updated_data):
    with open("rep2.json", "w", encoding="utf-8") as file:
        json.dump(updated_data, file, indent=2, sort_keys=True)

data_back(load())

# rep 3: deserialize 
api = '{"results": [{"id":1, "score": 9}, {"id": 2, "score": 7}], "count": 2}'
api_data = json.loads(api)
print(api_data)
print(api_data["results"][1]["score"])