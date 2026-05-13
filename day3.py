# Day 3: Lists (2nd most important data type in python after strings)

# python lists are automatically resizable 

numbers = [1, 3, 5]
numbers.append(4)
print(numbers) # while in C if you declare a list lets say
# int[10]; than you cannot change the length of the list 
# to do that you would have to create a new list.

# Some of the built in python methods 

nums = [3,5,5,6,4,7,9,8,1,2]
nums.sort()
nums.reverse()
nums.count(2) #
len(nums) # prints out the length of the lists, just as we used it in strings

# Part : 1 - what is list and how to create them
fruits = ["apple, banana, tomato"] # anything that is within the squared brackets is a list
empty = [] # this is called as an empty list.
# lists are unchanged like they are ordered the position inside the lists cannot be changed.

### Lists can hold any kind of data type unlinke that of a string. 
### which could only hold chars.
types = [1, "raghav", 1.32, True]
print(types)

### The third thing for the lists is that the lists are mutable
objects = ["Raghav"]
# objects.remove("R")
# print(objects) # this gives an error as we cannot change the strings 

# where as in a list
list_nums = ["Raghav", "KESHAV", "karana", "Happy"]
del list_nums[2] # removes the value at a defined index[] or a position
list_nums.remove("Happy") # we use this method to remove a specific value
list_nums.pop(0) # gives back the value which was removed and also that it only takes up INTEGER value not a string. 
print(list_nums) 

# just a quick checkup exercse 
my_numbers = [10, 20, 30, 40, 50]
my_numbers.append(60)
print(my_numbers)

my_numbers.remove(20)
print(my_numbers) # removes the value

my_numbers.pop(0) # removes what is there at the position
print(my_numbers)

del my_numbers[1] # also removes the stuff at the index which it has been told to. 
# for example here was at position 1
print(my_numbers)

# Most important fact of mutation is that in lists the most recent output becomes the input of the method.
# Tht is why lists are known to be mutable  

# Same drill 
fruit_ninja = ["apple", "banana", "cherry", "date"]

# fruit_ninja.append("melons")
# print(fruit_ninja)

removed = fruit_ninja.pop(0)
print(removed)
print(fruit_ninja)

# stack and queues 

# last in frst out is Stack (LIFO), and first in last out is queue (FIFO).
# both stack and queue uses python list.
# THE ONLY DIFF IS WHERE YOU REMOVE IT FROM.
# using .append() for both the stack and queue 
# as the keyword suggest it adds something and both the stack and queue use that.
# for queue think of append as the 1st costomer at the CAFE
# for stack think of it as the 1st PLATE from the pile of plates.

# REMOVING is the part where they differ
# STACK - last in first out :
game = ["ps4", "ps5", "Xbox"]
game.append("FIFA26")
game.pop() 
print(game)
# here we saw it working that the last one entered was the first one out
# basicaly .pop() is used for both the stack and queue data structures in python. 
# and when we do not pass any value in .pop() as it works on indexing positions
# so no indexing value in .pop meaning it is a stack which is again 
# LAST IN FIRST OUT

# QUEUE : First in first out: Like serving a customer in line.
consumer = ["jarrod", "gilfoyle", "dinesh", "richard"]
consumer.append("monica") # add and then the first one gets removed or gets served. FIFO
consumer.pop(0) # FIRST IN FIRST OUT or WE CAN SAY something with a value or indexing position inside is a QUEUE
# DATA STRUCTURE
print(consumer)
# basic gist of the queue data struc.