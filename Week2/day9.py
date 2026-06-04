# Day 9 Comprehensions
# So like how we use to add something lets say 
names = ["alice", "wonderland", "raghav"]
names_upper = [] # here we passed a empty store transformed values from the names list.
for n in names:
    names_upper.append(n.upper())
    print(names_upper) # here we are trying to store the uppercase values 

# but when we used a comprehension like .upper() we will write it as 
updates_names = [i.upper() for i in names] 
# now the abover version is the compresion version we donot need any empty list on top or at the bottom a function called .append()
# comprehension is a loop that builds and returns a collection, written as a single expression.

nums = [1,2,3,4,5]
squares = [n ** 2 for n in nums]
print(squares)

prices = [10, 20, 30]
with_tax = [price * 1.05 for price in prices]
print(with_tax)

# Part 2: FILTERING: ADDING A LAYERMOF CHECK LIKE iF
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
big = [n for n in numbers if n > 5]
print(big)

result = [num * 10 for num in nums if num % 2 == 0]
print(result)

# Exercises
## A.
words = ["hi", "hello", "hey", "howdy", "yo"]
short = [w for w in words if len(w) <= 3]
print(short) # a list of words less than or equal to 3 gets printed ["hi", "hey", "yo"]

## B.
nubs = [5, 12, 8, 21, 3, 16]
results = [n + 100 for n in nubs if n > 10]
print(results) # here 12, 21 and 16 gets passed and than we print [112, 121, 116] as a list

## c.
temps = [18, 25, 30, 12, 22, 35]
updated_temps = [t for t in temps if t >= 25]
print(updated_temps) # a list of temps gets updated and printed and [25,30,35] is the final value

# Part 3: Comprehensions with dictionaries
name = ["raghav", "bob", "charlie"]
length = {a: len(a) for a in name} # so here we are printing a dictionary
# with name as the key and the length of the name as value.

# Exercise D:
given_nums = [1, 2, 3, 4]
updated_squares = {n: n ** 2 for n in given_nums}
print(updated_squares) # this prints off squares of numbers with numbers against their squares

## E.
given_prices = {"apple": 2, "banana": 1, "cherry": 5}
doubled_prices = {k: v * 2 for k, v in given_prices.items()}
print(doubled_prices)

# Cumulative exercises:
## 1.
raw_tags = ["  Python ", "DATA", "python", "  data  ", "SQL"]
clean_tags = [r.lower().strip() for r in raw_tags]
print(clean_tags)

## 2.
unique_tags = {t.lower().strip() for t in raw_tags}
print(unique_tags)

## 3.
users = [
    {"name": "alice", "age": 30, "active": True},
    {"name": "bob", "age": 17, "active": False},
    {"name": "chalie", "age": 25, "active": True}
]

updated_users = [u["name"] for u in users if u["age"] >= 18]
print(updated_users)

# Exercise: Price + filter transform
products = [
    {"name": "mouse", "price": 25},
    {"name": "keyboard", "price": 75},
    {"name": "monitor", "price": 300},
    {"name": "cable", "price": 10},
]

naming_list = [n["name"] for n in products if n["price"] > 50]
print(naming_list)

# Dicts from two ideas
given_words = ["python", "data", "sql", "kafka"]
length_words = {word: len(word) for word in given_words if len(word) > 3}
print(length_words)

# Unique first letters
names_given = ["alice", "andrew", "bob", "brenda", "charlie", "anna"]
update = {e[0] for e in names_given}
print(update)

# Building from scratch:
scores = {"alice": 85, "bob": 42, "charlie": 90, "dave": 60}
passed = {f"{k}: {v}%" for k, v in scores.items() if v >= 60}
print(passed)

given_nums = [-4, -1, 0, 3, 10, -5, 2]
updated_nums = [i ** 2 for i in given_nums if i == 0 % 2]
print(updated_nums)