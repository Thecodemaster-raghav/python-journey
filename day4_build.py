# Day 4 Build challenge - Quiz Tracker with loops
# Date: May 20th, 2026

# Questions studets will attempt
questions = ["Q1: Beta blockes", "Q2: ACE inhibitors", "Q3: ARBs", "Q4: Diuretics", "Q5: Statins"]

# Whether each question was answered correctly (True = correct, False = wrong)
# This lines up with questions by  position: result[0] is for questions[0], etc
result = [True, False, True, False, True]

# Trcakers
answered = []
wrong_answers = []

for i in range(len(questions)): # we are checking the values here through indexing
    answered.append(questions[i]) # adding the values inside the questions as we do not need any conditions here
    if result[i] == False: # checking questions which were answered wrong
        wrong_answers.append(questions[i]) # adding the wrong_asnwered questions

correct = len(answered) - len(wrong_answers) 

print(f"Total answered: {len(answered)}")
print(f"Qestions to review: {wrong_answers}")
print(f"Score: {correct} / {len(answered)}")


# The architechtural structure till now here would be is :
# First we loop through the values inside of both questions and result. 
# We match if the question is answered using indexes at questions that is why we used range + len outside the loop.
# after that we needed to find which answers were wrong so put a condition using indexing as well.
# That means the questions which were answered wrong should be added into the wrong_answers list
# This is what i got till now. i took some help ofc.