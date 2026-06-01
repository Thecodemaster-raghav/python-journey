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
print(len((all_difficulties))) # 8
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
bookmarks.remove("Q5")
bookmarks.discard("Q99")
bookmarks.discard("Q12")
# bookmarks.remove("Q99") # here the code crashes KeyError
print(bookmarks) 

# Dedup count from a "File"
raw_log = ["cardio", "renal", "cardio", "neuro", "cardio", "renal", "endo", "neuro", "cardio"]
print(len(raw_log)) # total number of sessions
unique_subjects = set(raw_log)
print(len(unique_subjects)) # prints the number of unique subjects studied