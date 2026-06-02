# Here we are starting off with Sets and tuples: Day 8
# Sets are just unique set of values placed inside curl braces just as we did we the dictionaries
# for Example:
difficulty = {"easy", "hard", "easy", "hard", "good", "hard"}
# print(difficulty)
# so he we moticed that no duplicates we printed which means python enforces uniqueness in a set.

# Why do we need sets:
# It will deduplicate for us for free. Means that lets say a lists has duplicate values
# and we want to remove duplicates using set(variable) it will delete those duplicate values
# and will print off the unique values
# EXAMPLE:
raw = ["wasy", "hard", "easy", "good", "hard"]
unique = set(raw) # will print off the unique values and slash off all the duplicates.

# Reason 2: Using a set will also give us super fast membership checks
# So python used HASH TABLES FOR sets and dicts.

# Analogy: Sets = A labelled filing cabinet: To find a paper lets say from 2025 we check that drawer with files from
# 2025.

# For lists it is not the case for list it checks all the files which is very time consuming.

raw_difficulties = ["easy", "hard", "good", "easy"]
unique_val = set(raw_difficulties)
print(raw_difficulties)
print(unique_val)
print("hard" in unique_val) # this gives out a boolean value.
print("mediumish" in unique_val)

# we will use few operations none of these are new concepts.
# .add() will let us add a value to the set. But if the item is already in the set 
# .add() does nothing.
notes = {"read", "write"}
notes.add("store") # here . add will do its operation and add the value to the list.
print(notes)

# .remove() is used to remove the items. It is strict and needs the value to be there in the set.
# it is also case sensitive
# notes.remove("hard")
# print(notes)

# Checking memberships:
if "read" in notes:
    print("yes")

# when we want to check the length: same len()
print(len(notes))

# Sets cannot hold lists inside of it as it only holds immutable items.

# Exercise 1: Dedup a list
all_difficulties = ["easy", "hard", "easy", "good", "again", "hard", "easy", "good"]
# convert to set 
new_set = set(all_difficulties)
print(new_set)
print(len(  all_difficulties)) # 8
print(len(new_set)) # unique vals only so : 4

# Build a set from Scratch: 
tags = set()
tags.add("cardiology")
tags.add("endocrine")
tags.add("cardiology")
tags.add("renal") 
print(tags) # will only print 3 cardilogy, renal and endocrine

# Membership checks.
print("renal" in tags) # True
print("neurology" in tags) # False
print("cardiology" in tags) # True

# Remove vs Discard
bookmarks = {"Q1", "Q5", "Q9", "Q12"}
bookmarks.discard("Q5")
bookmarks.discard("Q99")
bookmarks.discard("Q12")
# bookmarks.remove("Q99") # here the code crashes KeyError
print(bookmarks) 

# Dedup count from a "File"
raw_log = ["cardio", "renal", "cardio", "neuro", "cardio", "renal", "endo", "neuro", "cardio", "endo"]
print(len(raw_log)) # total number of sessions
unique_subjects = set(raw_log)
print(len(unique_subjects)) # prints the number of unique subjects studied

# Part 3: St operations- UNION, INTERSECTION AND DIFFERENCE.
# union: everything from both bags combined
# difference: stuff that is 1 bag but not in the other bag:
# Intersection: Stuff that is is both bags.

# Syntax: 
cardio_ques = {"Q1", "Q3", "Q5", "Q7"}
renal_ques = {"Q3", "Q5", "Q8", "Q9"}

# UNION: EVERYTHING COMBINED
all_ques = cardio_ques | renal_ques # | this pipe symbol charcterises union
print(all_ques) # can also use cardio_quest.union(renal_ques)

# real worl scenario: How many unique questions does the sudent need to review

# Interssection:
shared = cardio_ques & renal_ques # Gives questions present in both cardio and renal
# or we can also use cardio_ques.intersection(renal_ques)
print(shared)

# Real world scenario: Which questions are cardio-renal questions. or 
# Which qpearls did the student see in both monday and tuesda's review sessions?

# Difference: Which is present in 1 but not the other 
cardio_only = cardio_ques - renal_ques # the -ve symbol
print(cardio_only) # gives back questions present in only cardio.

# so here it means that it taes everything in the right set and removes anything also in the right set.
# real world scenario: which easy_bank question has the student not answered yet. easy_bank - answered.
# this is the kind of operation our platform's question remaining feauture would o behind the scenes.
# 
# # tiny scenario:
# to get both we will use Intersection.
# to get the unique value we will use UNION 
# Difference: Done on monday but skipped on tuesday

# Exercies to lock in the concept.
monday_tags = {"cardio", "renal", "endo", "neuro"}
tuesday_tags = {"renal", "neuro", "ortho", "derm"}

# Findind all unique tags studied all wek
all_week = monday_tags.union(tuesday_tags) # since a unique value to find so we would use union
print(all_week) # {"cardio", "neuro", "renal", "derm", "ortho"}

# Tags studied on both days
both_days = monday_tags & tuesday_tags
print(both_days) # to find tags in both days we would use intersection. "renal" and "neuro"

# Tags for monday only
monday_only = monday_tags - tuesday_tags
print(monday_only) # just to get the monday tags and matching ones from tuesday

# only tuesday_tags
tuesday_only = tuesday_tags - monday_tags
print(tuesday_only) # here just the tags used on tuesday and the similar ones from monday wil get printed


# Real scenario: Questions remaning
easy_bank = {"Q1", "Q2", "Q3", "Q4", "Q5", "Q6", "Q7", "Q8"}
answered = {"Q2", "Q5", "Q7"}

remaining = easy_bank - answered # here we have used a difference. As we wanted to find something which is not in 
# answered
print(remaining)

progress_count = len(answered)
print(progress_count) # here i have used answered as those the questions the students have completed.

# Part 4: Tuples: Immutable like strings. But store collection of items 
# just as a list but we cannot add remove or add to it or modify any item in it. they are 
# frozen when created.
# we write tuple with parantheses:
# point = (1, 3)
person = ("raghav", 26, "saskatoon")
# we can access any items inside of a tuple using index[0, 1, 2]
# just as we did with a list
# print(point[0])
# print(person[0])

# we also loop over a tuple exactly like a list
for i in person:
    print(i)

# we can check memberships exactly like a list
# print("raghav" in person) # True

# so far it sounds like a list. The difference is what we cannot do.
# person[0] = 10 # will crash
# person.append("ai enfgineer") # will carsh

# tuples are read only after creation.

# but why do tuples exists when list is already there

# the biggest difference between a tuple and a list is that. once created 
# they are frozen we cannot change, modify, update or add to a tuple. they are immutable.
# while a list is not immutable.

# i will reach for a tuple when i want a set a values and i do not want them to change.
# like langitude and lantitude or a date. I do not want to change the format of how they are 
# stored.

# Part - 5: Tuple Unpacking.
# we do tuple unpacking so that a fucntion can return multiple values cleanly.

# tuple exercise:
user = ("raghav", 26, "saskatoon")
point = (3, 5)

# Basic indexing:
print(user[0]) # prints the name
print(user[2]) # prints the city

# Tuple unpacking
name, age, city = user # unpacks into all three

# Immutability proof:
# point[0] = 99 # will give a error stating 'tuple' object does not support item assignment.

# function returning a tuple:
def get_coords():
    numbers = 45.4, -75.6
    return numbers
lat, lng = get_coords()
print(lat, lng)

# underscore for dont care
def get_val(user):
    return user
name, _, city = get_val(user)
print(name, city)

# swap with tuple:
a= "first"
b = "second"
print(a, b)
# after swap
a, b = b, a
print(a, b) 

# looping over tuples in a list
students = [("alice", 92), ("bob", 78), ("raghav", 85)]
for name, score in students:
    print(f"name: {name} Score: {score}")

# real scenario: 
scores = [80, 92, 75, 88, 90]
def analyze_scores(scores):
    total = sum(scores)
    avg = total / len(scores)
    return total, avg
total, avg = analyze_scores(scores)
print(total, avg)