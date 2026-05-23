# Functions : The meaty ones
# Two halves: Defining the Function AND Calling the functions
# Defining it: Writing the recipe- This is just defining the code does not run in the defining block.
def greet(): # here we are just 1st definging the function then giving it a name 
    print("Namaste!")  # greet() in this case and then : after the colon a indented block of code.

greet() # this is calling the fnction what we just defined above.
# it will print Namaste

# Putng an input inside that of the function
def greet(name):
    print(f"Hello, {name}") # just like we did in an f string 

greet("raghav") # here we are calling greet function.
# name inside () is called a parameter - its a placeholder, meaning 
# it means when someone calls me, they'll hand me a value and i'll call that vlaye (name) inside here.
# it means nothing has a value yet and name is just a name waiting to be filled.
# now we call it using greet("raghav") like we did above.
# so when the argument = "raghav" is called it prints the output.

def add_label(topics): # here we are defining a function called add_label using topics as the input.
    print(f"Question topic: {topics}") # here topics is the parameter or placeholder for what we are calling with the fucntions 
    # which makes it a input to the function.
add_label("Cardilology") # so here we are calling the argument meaning adding a value called Cardiology.
add_label("Pharmacology") # same here we are calling the argument meaning adding a value called Pharmacoology.

def double(n):
    print(n * 3)

x = double(10)
print(x)
print(double(7))

# Part 5: Multiple parameters
# so far our function took only one input like def greet(name)
# but fucntions can take multiple parameteres
def fifa_worlcup(countries, players):
    return(f"{countries}: {players} jersey name")
# so like the above function has 2 parameters : countries and players
# so when we call the function we pass 2 parameters

# Piece 2: Local variables: mental rule: 
# A variable which is created inside a function stays inside that function only
# it is hidden from the outside world.
def calculate(a, b):
    total = a - b # here total is that local variable
    return total
calculate(10, 6)
print(calculate)
# print(total) # here we will get an error as total does not exist outside the function