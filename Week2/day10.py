# Day 10 error handling.
# indexerror: print([1, 2, 3][5]) 
# it would give an exception somthing like cannot print list in a tuple. # IndexError
# print(10/ 0)
# it would print something like number not devisible or a ZeroDevisionError.
# print(int("hello"))
# python would give an error stating that cannot convert int to str. #ValueError

# Concept 2: try/except: 
# this means that in the upper case when we got an error our program crashed.
# the whole program stopped running.
# But with the try and except block we can say to python that do not crash try this if this blows up
# except this instead.
# for example
try:
    #code that might raise an error
    print(10/0)
except:
    # do this instead if the try block crashes
    print("cannot devide by zero!")

# key idea for this is that we are not preventing the error we are catching it.
print("start")
try:
    print(10/0)
    print("this line is inside try block!")
except:
    print("we caught the error")
print("end")

# Concept 3: Catching the right error:
# this means that except ZeroDevisonError wil oly catch one type.
# lets see this in an example.
print("start")
# try:
#    print(int("hello"))
# except ZeroDivisionError:
#    print("the error is here in this line")
# print("end")
# so in this block of code we saw that the except block handles the type of error that is given to it.
# and if we do not give any type the except block would run but if there is a type of error like
# the ZeroDevision error passed with the except block than the code will crash.

# so the principle here is to be specific about what we catch and the unexpected crash.
# as a unexpected crash is the information and bare except is SILENCING THE CRASH

# CONCEPT 4: Else and Finally

try:
    print(10/2)
except ZeroDivisionError:
    print("Error Caught!")
else:
    print("no error happended")
finally:
    print("done")

# Concept 5: RAISING AN ERROR:
# Throwing your own errors:
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
# here python does not know that the age cannot be negative it will do what it is told to do.
# but with our knowledge we can raise an error where we think an error might arise and 
# python can misread that error.
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount

# call 1
print(withdraw(100, 40)) # this would perfectly fine and return 60.
# call 2
try:
    print(withdraw(100, 200))
except ValueError:
    print("Not Sufficient Funds") # this would go and reach out for that valueError insufficient funds