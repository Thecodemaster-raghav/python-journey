names = ["arjun", "priya", "dev"]

def update():
    for n in names:
        if n == "priya":
            m = names.index(n) # asks what is the position of n inside the list
            names[m] = "shriyam" # updates the data at that position
            return names
        
result = update()
print(result)
            
