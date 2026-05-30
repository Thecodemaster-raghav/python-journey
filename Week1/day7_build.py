# Day 7 : Build challenge # Pearls ETL
# Design
# 1st. Functions: there will be 2 functions one will take in the dictionary and the other we will use to count 
# calculate() function is the closest.

# .split will be used to split the string into parts. it would give back a string and then i will loop over the line 
# and then will grab the items and will count it using dictionary

# i will use an if condition to increase the count of the dictionary using .items() and wil increase the counter 
# as the loop will move ahead.

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
print(result)

def write_report(results, total):
    with open("pearls_report.txt", "w") as g:
        g.write("Pearls report\n")
        g.write(f"Total pearls: {total}\n")
        for k, v in results.items():
            g.write(f"{k}: {v}\n")
total = sum(result.values())
write_report(result, total)