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
        return "Raghav is a Loser but he will accomplish his dreams"
    return inner # here the nested function rule meaning when we call the outer() func it will return what it is being passed on.

nest_func = outer()
print(nest_func())