# Day 3 build challenge - Mini Quiz Tracker
# May 18th 2026

# Questions the student is about to attempt (in order)
upcoming_questions = ["Q1: Beta blockers", "Q2: ACE inhibitors", "Q3: ARBS", "Q4: Diuretics", "Q5: Stains"]

# Tracking answers
answered = []

# Tracking which questions they got wrong
wrong_answers = []

# SCRIPT
print(f"First question: {upcoming_questions[0]}")

# Step 2
correctly_ans = upcoming_questions.pop(0) # removing it and then adding it to 
# using queue here first question then answered firt and then took it out.
answered.append(correctly_ans) # storing that student has answered question 1 


# Step 3 : ans que 2 wrong
wrong = upcoming_questions.pop(0) # takes the question from the list and moves it to variable wrong
answered.append(wrong) # add the question which was answered 
wrong_answers.append(wrong) # adds the removed index from upcoming questions list


# Step 4 : ans que 3 correctly
correctly_ans = upcoming_questions.pop(0) # queue operation (first in first out)
answered.append(correctly_ans)


# Step 5 : typo fix
wrong_answers[0] = "Q2: ACE inhibitors (TYPO FIX)" # changing a perticular value in a list. mutation concept

# Step 6 : Summary
print(f"Remaining questions: {upcoming_questions}") # prints the number left in the list
print(f"Answered so far: {answered}") # prints the answered list
print(f"Need to review: {wrong_answers}") # prints the wrong asnwer list
print(f"Numbers answered: {len(answered)}") # print the length of the answered list