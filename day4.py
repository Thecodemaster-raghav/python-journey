# If else and loops + integrating this into mini quiz tracker 

# How if and else work.
# when we write if and else it is meant from an engineering 
# POV that: IF THIS IS TRUE do X, if not then do Y. 
# The main gist is : to make decisions.

# simple syntax
age_r = 26
if age_r >= 18: # here it means in this line of code that if the age needs to be greater or equal to 18
    # for this to work or the statement goes to else block. If the above statement is not true.
    print("you can vote")
else:
    print("Cannot vote")

# this is an example of elif : which means multiple branches of if 
game = ["fifa", "gta"]

if "fifa" in game:
    print("n/a")
elif "gta" in game:
    print("b")
elif game.append("make"):
    print(game)
else:
    print("error")

# For loops : repeating eveything

# basic syntax

my_fruits = ["apple", "banana", "cherry"]
for my_fruits in my_fruits:
    print(my_fruits)


# for repeating the number N times we use range() ex
for i in range(6):
    print("AI engineer") # so here it prints off AI engineer 6 times

# meaning the loop would run 6 times and then it would escape the block.
# but the the indexing remains the same. runs from 0 to 6

# i is a conventional variable name for a loop counter it stands for index.
# use it when looping over numbers

# doubling the nums_second using
nums = [1, 2, 3, 4, 5]
nums_second = []

for n in nums:
    nums_second.append(n * 2)

print(nums_second)


# Quick examples to solve before moving ahead

animals = ["cat", "dog", "bird"]
for a in animals:
    print(a)

# Block b
for i in range(4):
    print(i)

# Block c
nums = [10, 20, 30]
total = 0

for n in nums:
    total = total + n # in this variables outside the loop keep their values between iterations
    # their values does not reset 
    # as in the above case for the first iteration total = 0 and for the sec one it would be 
    # total = 10  not 0 as it does not change values.
    # It means each iteration uses whatever was the total at the end.
print(total)

count = 0
for i in range(4):
    count = count + 1
print(count)

fruit_names = ["banana", "cherry", "starwberry"]
collected_fruits = []

for f in fruit_names:
    collected_fruits.append(f)
print(collected_fruits)

numbers = [1, 2, 3, 4, 5, 6]
biggest = 0
for n in numbers: # so here the n is the temporary variable and whenever n= something, biggest will also = something
# so that means at the end of the loop where n= 6 then biggest = 6 and there the loop ends
# so as there is nothing left in the loop the n comes out and like that we get biggest = 6.
# not by comparing which on is the biggest.
    biggest = n
print(biggest)

# so to find the biggest number we would need to some kind of check or codition 
# inside the loop for that w will use IF statement.

# part 3 : While Loops
# Runs up and until the condition is true 
# basic syntax
count_nums = 0
while count_nums<5:
    print(count_nums)
    count_nums = count_nums + 1

# Part 4: Now combining if/else with loops.
# there are three conditions we use if and els inside a loop
# counting:  Lets say a list of nums we have to find which one is greater than which number.
# so we set up a accumlator variable which will collect the evidence of or condition
# which here is counting.
nums_list = [22, 33, 24, 58, 62, 27, 48]
counted_list = 0
for n in nums_list:
    if n >= 50:
        counted_list = counted_list + 1 # here we gave the condition to count
print(counted_list)
# counting =  add 1 each time something matches.

# Filtering
# Filtering means when we have to collect the items that match our condition
# and store them in a new list

old_list = [58, 65, 98, 200, 100]
new_list = []
for o in old_list:
    if o >= 60:
        new_list.append(o)
print(new_list)

# Findinf : Which means we will be finding if the value is max, min or a specific value using conditions

given_values = [78, 33, 55, 20, 59]
max_val = 0
for maximum in given_values:
    if maximum > max_val: # here max is comparing with 0 so for the 1st time the loop runs max = 78
        # which is of course greater than 0 and after that it adds it to max_val: accumlator variable
        # and after that 33 = max, which is not greater than 78. and that is the gist of this algorithm
        max_val = maximum 
print(max_val)