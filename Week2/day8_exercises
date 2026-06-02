# Day 8 Exercises

# 1. 
languages = ["python", "java", "python", "go", "java", "python"]
unique_languages = set(languages) # using set data structure as we do not have to count anuthing unlese would have used a dict
print(unique_languages)

# 2. 
nums = [42, 17, 88, 3, 56, 91, 24]

def min_max(nums):
    smallest = nums[0]
    largest = nums[0]
    for n in nums:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest
smallest, largest = min_max(nums)
print(smallest, largest)

# 3.
monday = {"cardio", "renal", "neuro"}
tuesday = {"renal", "neuro", "endo", "derm"}
wednesday = {"cardio", "endo", "ortho"}
# will set operations like intersection here as we want everything.
two_tags = monday.intersection(tuesday).intersection(wednesday) # it means no overlap exists
# as wednesday has no value matching to the other two days.

# 4.
contacts = [("alice", "555-0001"), ("bob", "555-0002"), ("raghav", "555-0003")]
for name, phone in contacts:
    print(f"{name} number is {phone}")

# 5.
session_1 = ["Q1", "Q3", "Q5", "Q3", "Q7", "Q1"]
session_2 = ["Q2", "Q5", "Q9", "Q5", "Q11"]

# USING UINON and intersection SET OPERATION 
first_session = set(session_1)
second_session = set(session_2)
# converting to set first
unique_questions = first_session | second_session # Union
both_session = first_session & second_session # intersection
print(unique_questions)
print(both_session)

# 6.
name = "raghav"
numbers = [78, 92, 85, 90]
def student_summary(name, numbers):
    average = sum(numbers) / len(numbers)
    highest = max(numbers)
    return name, average, highest
name, average, highest = student_summary(name, numbers)
print(name, average, highest)

# 7.
# for exercise 7 i will be using set and dict data structure as we are mapping. and the value side is 
# what i do not want to change so tuples in values
bookmarks = {
    "raghav": {"Q1", "Q3", "Q5"},
    "manoj": {"Q3", "Q5"},
    "keshav": {"Q5", "Q4", "Q6"}
}

# check for specific question
check = "Q4" in bookmarks["keshav"]
print(check)
# printing all bookmarks one user
print(bookmarks["manoj"])

# 8. Real world scenario
reviews = [
("P1", "Easy", True),
("P2", "Hard", False),
("P3", "Easy", True),
("P1", "Easy", True),
("P4", "Good", False),
("P2", "Hard", True),
]

total_reviews = len(reviews)
print(total_reviews)
# to find the unique perals count or number of unique pearls
unique_pearls = set() # first we will put a set here to collect the values
for pearl_id, difficulty, was_correct in reviews:
    unique_pearls.add(pearl_id)
print(len(unique_pearls))

wrong_pearls = set() # same here we used an empty set then a condition to find out whoch pearl_id's were false atleast once
for pearl_id, difficulty, was_correct in reviews:
    if was_correct == False:
        wrong_pearls.add(pearl_id)
print(wrong_pearls)