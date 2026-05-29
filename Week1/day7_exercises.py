# Exercise 1: Read the whole file
# with open("sample.txt") as f:
#    content = f.read() # reading the whole file
#    print(content)

# Exercise 2: Loop line by line and Exercise 3: Clean each line with strip()
with open("sample.txt") as f:
    for line in f:
        print(line)
        print(line.strip()) # here there are no spaces left as no newline chars that is why we use .strip to clean
         # here every line gets printed with a newline character. that is part of the string.

# Exercise 4: Read all lines into a list
with open("sample.txt") as f:
    text = f.readlines() # reads the whole file into a list of strings
    print(text) # would print a list ['grocery 200\n', 'transport 150\n', 'rent 400']
    print(text[0]) # here the item at index 1st would get printed which is ['grocery 200']

# Exercise 5: Write into a new file
with open("output.txt", "w") as w:
    w.write("Day 7\n")
    w.write("Exercises\n")
    w.write("Done\n")

# Exercise 6: Append vs Write
with open("output.txt", "w") as w:
    w.write("Day 7\n")
    w.write("Exercises\n")
    w.write("Done\n")

with open("output.txt", "a") as w: # both the "w" runs it wiped and rewrote the the identical content
    # that is why the file looks unchanged. Then "a" added on top of "w" gives 6 lines
    w.write("Day 7\n")
    w.write("Exercises\n")
    w.write("Done\n")


# Exercis 7: Read and proces the lines
count = 0
with open("sample.txt") as x:
    for i in x:
        count = count + 1
        print(count) # it would print nums like 1, 2, 3 as i have not done readline() to make it list first as it was not asked.

# Exercise 8: safe read with os.path:
import os
if os.path.exists("sample.txt"): # condition to check whether this file exists or not
    with open("sample.txt") as f:
        file = f.read()
        print(file)
else:
    print("File not found") 

# 2nd Run:
import os
if os.path.exists("nonexistent.txt"): 
    with open("nenexistent.txt.txt") as f:
        file = f.read()
        print(file)
else:
    print("File not found") # it would run the else block as there is no nonexistent file present.