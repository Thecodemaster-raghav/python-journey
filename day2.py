# Day 2 Officially starting off string
# Date: 03 may 2026

# String character example
name = "Raghav"
print(name[1])

# Counting BACKWARDS using -ve numbers
print(name[-1])
print(name[-2])
print(name[-5])

# Positive indexing: not the way to go to
# Lets say: we Want last three char using positive indexing

my_name = "Keshav"
length = len(my_name)
last_three = my_name[length -3: length]
print(last_three)

# In this case we had to measure the length of the string first with len()
# Than we had to do subtraction using length - 3 and then we had to slice.
# Takes a lot of space and time if we do it like this 

# Instead we can do NEGATIVE INDEXING to get a more optimized solution
# As with negative indexing we do not need to know the length at all
# Here we just said give me the last 3 or last 2 
# we did not use len() or slice or math
# Just python counting from the end automatically when using -ve indexing 

my_name_2 = "Happy"
last_two = my_name_2[-2:]
print(last_two)

# Example 2 
email = "raghav563@gmail.com"
# get the last 9 characters gmail.com
last_nine = email[-9:]
print(last_nine)

# Full slicing syntax
# string[start : end]
# example : name = "Raghav"
# print(1:4)
# here python will print index from 1 to 4
# Deeper meaning : it means the starting position is index 1 and the : = range (how many we want), 4 = till 4th position or index 4


# Part 2 : Slicing

name2 = "Veena"
print(name2[:3])
print(name2[-3:])

text = "Engineering"

print(text[0:4])

# Part 3: Length and in

my_length = "Length"
print(len(my_length)) # here we are using len() which prints out the length of the variable inside the curved braces.

# in operator
message = "I love python programming."
print("python" in message)
print("java" in message) # when we use an in operator it returns a boolean.

# Actual use case scenario:

# example from claude: Validate email format:
email_format = "raghavsharma@gmail.com"
if "@" in email_format:
    print("It is correct format.")

# another example : Check file type:
file_name = "report.pdf"
if ".pdf" in file_name:
    print("LOoks like a pdf to me.")

# In AI engineering specifically len() fits in where we want to check the
# length of the prompt. 
# Such as to check whether it fits in the token limit? 


# So here we saw the variable user_input being returned as an int 
# len() is a fucn which will work well with the integer type and the use case is we have discussed above.
# in the real world scenario.
# IN also works like that usually when we are doing RAG scenarios it will do the checking of the keyword such as "well"
# and wil return the most suitabe response 


user_input = "This fits in well inside the token"
length_input = len(user_input)
print(length_input)
if "well" in user_input:
    print("Yes it is true")
else:
    print("false")

# Part 4: String methods: The daily toolkit and method chaining.

my_text = "  shriyam is my girlfriend "
my_output = my_text.strip().lower()
print(my_output) # so what .strip() it removes extra spaces from beginning and the end.

# But does not remove spaces from the middle of the string and 
# .lower() converts the output to a lower case string before returning.

# in method chaining we have strings method doing the work. 
# like in the example we have two methods calling .strip() and .lower()
# chaining is calling the method on what the prev method returned.
# so like in the above ex: .strip() returned "shriyam is my grirlfriend."
# and the then the output was used for the method .lower()
# and it returned the final output "shriyam is my girlfriend" in lower case.

# Exercise 1 : Indexing basics 
my_string = "Programming"
print(my_string[0]) # prints the first character of the string.
print(my_string[-1]) # prints the last char of index[]
print(my_string[3]) # prints the 4th char
print(my_string[-2])

# Exercise 2: Slicing practice
given_string = "Programming"
print(given_string[:4]) # chars from index 0 to 4
print(given_string[-4:]) # chars from index -4 to last
print(given_string[3:7]) # chars from index 3rd to 7th and will not include the 7th char
print(given_string[2:]) 

