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
