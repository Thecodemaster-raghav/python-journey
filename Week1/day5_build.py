# Quiz tracker refractor : day 5 build challenge
questions = ["Q1: Beta blockes", "Q2: ACE inhibitors", "Q3: ARBs", "Q4: Diuretics", "Q5: Statins"]

result = [True, False, True, False, True]

def given_ques(questions, result):# definig a function with 2 parameters called question and result.
    answered = [] # two empty lists
    wrong_ans = [] 
    for i in range(len(questions)): # looping over the range of questions for comparing it with another list simoultaneously. 
        answered.append(questions[i]) # same concept of appending which is methods 
        if result[i] == False: # a condition to check and pass the results
            wrong_ans.append(questions[i]) # adding the values which match the condition to a list
    return answered, wrong_ans # storing these values until someone calls these values.

def calculate(answered, wrong_ans): # calculating the score using functions
    score = len(answered) - len(wrong_ans)
    return score # again storing the value until the fucntion is called 

def main():
    answered, wrong_ans = given_ques(questions, result) # in the main() where we are calling 2 functions simultaneously
    # the names beign filled goes onto the left and function goes to the right
    print(f"Total answered: {len(answered)}")
    print(f"Questions to review: {wrong_ans}")
    print(f"Score: {calculate(answered, wrong_ans)} / {len(answered)}")

main()
