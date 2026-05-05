# Day 2 Officially starting off string
# Date: 03 may 2026

# String character example
name = "Raghav"
print(name[1])

# Counting BACKWARDS using -ve numbers
print(name[-1])
print(name[-2])
print(name[-5])

# Positive indexing: not the way to go to
# Lets say: we Want last three char using positive indexing

my_name = "Keshav"
length = len(my_name)
last_three = my_name[length -3: length]
print(last_three)

# In this case we had to measure the length of the string first with len()
# Than we had to do subtraction using length - 3 and then we had to slice.
# Takes a lot of space and time if we do it like this 

# Instead we can do NEGATIVE INDEXING to get a more optimized solution
# As with negative indexing we do not need to know the length at all
# Here we just said give me the last 3 or last 2 
# we did not use len() or slice or math
# Just python counting from the end automatically when using -ve indexing 

my_name_2 = "Happy"
last_two = my_name_2[-2:]
print(last_two)

# Example 2 
email = "raghav563@gmail.com"
# get the last 9 characters gmail.com
last_nine = email[-9:]
print(last_nine)

# Full slicing syntax
# string[start : end]
# example : name = "Raghav"
# print(1:4)
# here python will print index from 1 to 4
# Deeper meaning : it means the starting position is index 1 and the : = range (how many we want), 4 = till 4th position or index 4
