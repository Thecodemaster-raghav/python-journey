# Day 7 : Build challenge # Pearls ETL
# Design
# 1st. Functions: there will be 2 functions in one function i will pass the argument like filename,  just so i can resuse it.
# the other fucntion will be used for writing and the 1st one is used for reading the file and performing actions.

# .split will be used to split the string into parts. but first i will use .strip to remove the extra spaces and then
# we grab the values from the dictionary that matches our output and update the count.

# then after that in the second fucntion we will write it using "w" the write operation and 
# then call it but also i will have to use 2 parameters like lets say results, total as we are calculating the total.

# read and write should be separate as it would be cleaner and we will be able to see all the opeations working.

def process_pearl(filename):
    count = {}
    with open("pearls_raw.txt") as f:
        for i in f:
            clean_data = i.strip()
            text = clean_data.split(" | ")
            difficulty = text[1]
            if difficulty in count:
                count[difficulty] = count[difficulty] + 1
            else:
                count[difficulty] = 1
    return count
result = process_pearl("pearls_raw.txt")

def write_report(result, total):
    with open("pearls_report.txt", "w") as w:
        w.write("Pearls report\n")
        w.write(f"Total pearls: {total}\n")
        for k, v in result.items():
            w.write(f"{k} : {v}\n")
total = sum(result.values())
write_report(result, total)

