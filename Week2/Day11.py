# Day 11 Modules and imports
# imports are used to get python modules 

# how it works:
import math # here math is a built in python module that is being called

square = math.sqrt(16) # so here .sqrt is a function living inside the math module
# . prefix is important as it tells python here to find 
print(square)

# now the exercise
print(math.sqrt(25)) # this will print 5
print(f"{math.pi:.2f}") # this will print the value of pi = 3.14

# here we are just grabing the specific functions that we need from the math module.
from math import sqrt, pi
print(sqrt(49))
print(pi) # just a convinient way of writing 

# now the one that matters in my own projects 
# importing your own files
import helpers
try: 
    get_result = helpers.doubled(10) # so it wil ask the user to give the inout as i have written int(input()) in helpers.py
    print(get_result)
except TypeError:
    print("Please provide input with the function as well")


# Exercise: Built - in module practice.
import random
print(random.randint(1,10)) # numbers between 0 to 9 will get printed.
print(random.choice(["apple", "banana", "kiwi"])) # python will choose randomly what to pick.

# 11.5: from import
from random import randint
print(randint(1, 100)) # will print any num from 0 to 100 range 

# 11.6: Dattime module
from datetime import datetime
now = datetime.now() # tells us the time right now using our local machine
print(now)
