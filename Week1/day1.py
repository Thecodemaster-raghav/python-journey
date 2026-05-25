#age  = 26 
# name  = "Raghav" # python is a dynamically typed language this i what is sjown here

#print(type(age))
# so as we see here we can check the what type of data type is being used here.
#print("Hello Raghav. Day 1  of the 6 months begins from now.")

age_2 = 28 + 3

print(age_2) # these are simple arithmati operators 
# there are mainly 3 types of operators which we are going to cover today

integr = 10 / 3

print(integr) # float type here is what we have used as data type 

share = 10 // 3

print(share) # here we have used the float or integer devision which will round of this value to the closest int value

# will be usefull when someone wants to know how many hours will there be in 7384 seconds. Where we would want a whole number value.
exponent = 2 ** 3 # this operator will raise the number to a power.
print(exponent) 

# Comparison operators (Rturn True or False depending on the value in the variable)
asha = 25
has_license = True

can_drive = asha >= 18 and has_license
can_vote = asha >= 18 or asha == 17
is_minor = not (asha <= 17)

print(can_drive)
print(can_vote)
print(is_minor)

name = 10%2 # % this is called the modulo operator. It gives what is left after devision for example when we do 10 / 3 the remainder is 1 so it will print that
print(name) 

# Key take away from this is that the even numbers always gives you 0 when moded by 2

my_age = 26 
my_age_after = my_age + 10

legal_age_drinking = my_age >= 25 
mot_legal = my_age <= 25 or my_age == 25

match_score = 10 % 2 
print(match_score)

# type conversion 
ke = "28"
# user_input = int(ke) 
# print(ke + 5)

# Building string from numbers 
score = 95
mesg = "raghav has " + str(score)
print(mesg)

user_input = " "
if user_input:
    print("Got input")
else:
    print("No Input")



# implicit coversion. Where python calls bool automatically and does the conversion for you
input4 = "Raghav"
if input4:
    print("Right Answer")

myself = ""

# since it is an empty string so if the string it is falsy
if myself:
    print("Got it")
else:
    print("Naah")

name1 = "Raghav"
Age1 = 26
Profession = "Gen ai engineer"
city = "ambala"

print(f"I am {name1}, i am {Age1}, working as a {Profession}, in {city}.")

# Excercise 2

my_int = 26
my_float = 2.0
my_str = "Raghav"
my_bool = True
my_none = None

print(f"Value: {my_int}, Type: {type(my_int)}", f"Value: {my_str}, Type: {type(my_str)}", f"Value: {my_float}, Type: {type(my_float)}", f"Value: {my_bool}, Type: {type(my_bool)}")

# Exercise 3 : The Tip Calculator

bill = 850
tip_percentage = 18
total_amount = bill * tip_percentage/100
total = bill + total_amount

print(f"The tip amount: {total_amount:.2f}")
print(f"The Total: {total:.2f}")

# Exercise 4 seconds calculator

total_sec = 7384
hours = total_sec // 3600
remaining_sec = total_sec % 3600

# pulling from the leftover
minutes = remaining_sec // 60
sec = remaining_sec % 60

print(f"{hours} hours", f"{minutes} minutes", f"{sec} seconds.")

# exercise 5 String to Numbers

str = "42"
integer = int(str)
total = integer * 3

print(f"Result: {total}")

# Exercise 8 : Temperature Converter

temperature_celsius = 36.5

temperature_fahrenheit = temperature_celsius * 9/5 + 32

print(f"{temperature_celsius}°C is {temperature_fahrenheit:.1f}°F")

# Exercise 9: : The Mystery Operator

print(f"{7 ** 0.5:.2f}") 
# When the exponent is 0.5, ** will calculate the square root.
# Because in math x ** (1/2) is same is square root of x.
# Example: 9 ** 0.5 = 3, 16 ** 0.5 = 4, 25 ** 0.5 = 5
print(9 ** 0.5)
# So like here we got the square root of 9 which is 3.
# This exercise was for getting the math running behind an exponential operator.

# Exercise 10: Case-Insensitive Password Match

user_password = "secret123"
user_input = "Secret123"

print(user_password.lower() == user_input.lower())

# No need to use If else the question was to run the code in 1 line.
# If/Else i used from our boolean case where we were checking 
# If the boolean would return false or true use "" empty string.
# So i from there i thought we could use that but i have learned 
# That we do not need to complicate tasks engineering is about not complicating but unwrapping.
