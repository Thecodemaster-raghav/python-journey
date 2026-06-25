# Day 7 - File input output: reading from and writing to files
# before we were hardcoding everything. But with File I/O (input / output)
# in simpler terms it writes the data inside lets say a file on the disk.
# the just not stays in the memory it stays inside of the file where we can revisit it.
# File I/O is the programs ability to read from and write to the notebook.
# so data can outlive a single run
# the tool we use for this is the open() function and the modern way to use it is the WITH statement

with open("data.txt") as f:
    contents = f.read()
# important : f only lives inside the indented WITH block 
# WITH is a special CONSTRUCT that does cleanup a regular block does not performs that action.

with open("data.txt") as f:
    text = f.read() #this .read() reads the whole file as a one bi string and the reads the newline chars /n 
    # as well. goOD for short files or when we want the raw content. Bad for big files

# WAY 2: .readlines() - it reads the whole file into a lists of strings, ONE PER LINE
with open("data.txt") as f:
    etxt = f.readlines()

# WAY 3: LOOP THE FILE DIRECTLY : one line at a time
with open("data.txt") as f:
    for g in f:
        print(g) # the cleanest way to do it. which means it oes not load the file at once
# it reads line by line. even the newline /n

with open("data.txt") as f:
    for g in f:
        cleaned = g.strip()
    print(cleaned)

# PART 3: Writing to a file 
# reading takes data out writing takes data in.
# in writing we tell open() by passing a second argument that we want to write using "w"
# "a" using append - meaning adding to the file 

with open("data.txt", "w") as f:
    f.write("hello\n")
    f.write("Saved: 250\n")

# 3 things to know here
# "w" is second argument to open() which means open for writing
# "w" wipes the file clean first. lets say if data.txt file exists before with contents
# opening it in "w" deletes what was there before writing to it.
# another thing is that we have to use /n to add a line between reading the data.

with open("output.txt", "a") as f:
    f.write("new data\n") # this would add to the end of the new data.

# part 4: FILE PATHS AND THE FILE DOES NOT EXIST PROBLEM.
# READING A FILE THAT DOES NOT EXIST
with open("output.txt") as o:
    text = o.read()
# here if the file does not exist python will give the error that file does not exist

# but if we do a write operaation with open() than python will create a new .txt file with 
# append operator "a"
with open("new_file.txt", "w") as f:
    f.write("Hello\n")  
# in this case python will create a new file and writes into it with "a" mode
# write never crashes on file never exists only read does.

# here we are using a if condition to check whether or not the file exists.
import os
if os.path.exists("new_file.txt"): # this returns True or False. os is build in tool kit 
    # and os.path.exists() to check whether this file is present or not
    with open("new_file.txt") as f:
        text = f.read()
else:
    print("file does not exist")


# Part 4 : Check:
#1st. if "data.txt" file does not exist. than if we try and open it. we will run into an error like File not found.

# and if we perform a "w" meaning a write operation using with open("data.txt", "w") as f: . Python sense that we asking it to 
# create a new file. and we can write into that using "a" -> which is the append operation.

#3rd. os.path.exists() is a useful operation to check before if a file exists or not. and not so useful 
# before writing is because in write "w" python creates a file itself so if we do not know that the fle exists or not 
# than it becomes useless to write as python wil by defalut create a new file if "w" operation is used.

# for both os.path.exists() and key in dict. are used to check whether lets say in files it checks that if the
# the file exists or not and same way: key in dic was used to check whether the key existed in the dictionary or no.