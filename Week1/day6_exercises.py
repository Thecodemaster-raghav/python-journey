# Exercise 1- day 6 - Read and print
# to print the capital of japan
capital = {"India": "New Delhi", "France": "Paris", "Japan": "Tokyo"}
print(capital["Japan"]) # here we have printed the capital of japan. "Japan" is important since if not used like that
# python thinks of it as a separate variable and there is a error

# Exercise 2: Add and Update
stock = {"apple": 5, "bananas": 8}
stock["apple"] = 10 # Updating apples
stock["oranges"] = 12 # adding oranges as a key value pair
print(stock) # now printing the stock dict.
# {'apple': 10, 'bananas': 8, 'oranges': 12} - final output

# Exercise 3: Safe Lookup with in
scores = {"maths": 90, "science": 85}
if "english" in scores: # first checking whether it is or not.
    print(scores["english"]) # printing value of english if it is in the dict.
else:
    print("No score for english") # print else if "english" not in scores


# Exercise 4: Loop and print all pairs
prices = {"pen": 10, "notebook": 45, "eraser": 5}
for p, v in prices.items(): # using the loop to check over over keys and values using .items
    print(f"{p} costs {v}") # printing them using an f string

# Exercise 5 : Count with a loop
results = {"Q1": True, "Q2": False, "Q3": True, "Q4": True, "Q5": False}
count = 0
for i in results:
    if results[i] == True: # this part i got stuck to check the values off of the keys here.  Which i asked for a hint
        count = count + 1 # increasing the count by 1 
print(count)

# Exercise 6: Building a Dictionary from scratch:

inventory = {}
inventory["apples"] = 10
inventory["cherry's"] = 23
inventory["kiwi's"] = 25
print(inventory) # we can build dictionaryup by ourselves it does not have to start full.

# Exercise 7: Find a specific thing in a loop:
ages = {"Raghav": 27, "Aisha": 31, "Vikram": 24, "Meera": 29}
for i, v in ages.items():
    if v > 28: # checking age using v as value and if the age is greater than 28 or not.
        print(i)

# Exercise 8: Sum the values
cart = {"shirt": 500, "jeans": 1200, "shoes": 2000}
total = 0
for c, v in cart.items():
    total = v + total # neede a running total. was just a minor stuck i did the hard part
print(total)

# Exercise 9: Two dicts,  parellel lookup
questions = {"Q1": "Capital of France", "Q2": "Largest planet"}
answers = {"Q1": "Paris", "Q2": "Jupiter"}

for q in questions:
    print(f"{q}: {questions[q]} -> {answers[q]}")

