# A side roject a very simple one where i track my monthly expenses
# Tech stack - Going to use loops fucntions and dictionary data structure and lists as well.
# a very simple hard coded expense tracker which tarcks y expenses.

salary = 2600
expenses = {"grocery": 200, "transport": 150, "sendhome": 1300, "bills": 300, "rent": 400}

def sum_expenses(expenses):
    total = 0
    for e, v in expenses.items():
        total = v + total # checking the total of the values inside expenses
    return total

def amount_saved(salary, total):
    saved = salary - total # to check the left amount after all expenses
    return saved

def main():
    total = sum_expenses(expenses)
    saved = amount_saved(salary, total)
    print(f"Amount saved: {saved}") # here checking how much is left using a main() function and calling the 2 funtions
    # using 2 variables 

main()