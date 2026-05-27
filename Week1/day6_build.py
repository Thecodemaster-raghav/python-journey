# Day 6 : Build challenege : Refractor Quiz Tracker and Engineering Review

# DESIGN : 
# instead of Lists it will be a simple 1 dictionary.
# That will have the keys as questions and True or False as values.
# In the first function using only 1 dict as inputs we will call 2 more lists
# For all the asnwered questions and the ones which were wrongly answered
# we would put in them and then we put a loop on the questions dict.
# we will then call another function and will name it calculate and use the above lists answered and wrong_ans
# to calculate how any were answered and how many need reviewing and total answered.

questions = {"Q1: Beta blockes": True, "Q2: ACE inhibitors": False, "Q3: ARBs": True, "Q4: Diuretics": False, "Q5: Statins": True}
# this is how the keys and values would look like insde the questions dict

def process_results(questions):
    answered = []
    wrongly_ans = []
    for q, v in questions.items():
        answered.append(q)
        if v == False:
            wrongly_ans.append(q)
    return answered, wrongly_ans

def calculate(answered, wrongly_ans):
    score = len(answered) - len(wrongly_ans)
    return score

def main():
    answered, wrongly_ans = process_results(questions)
    print(f"Total answered: {len(answered)}")
    print(f"Questions to review: {wrongly_ans}")
    print(f"Score: {calculate(answered, wrongly_ans)} / {len(answered)}")

main()

