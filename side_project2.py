# an expense tracker that tracks your transactions and flags if savings went low.
# the simple design build login-> enter salary-> add transactions-> recompute savings-> warn if low
from datetime import datetime
class Transaction:
    def __init__(self, amount, date, type):
        self.amount = int(amount)
        self.date = date
        self.type = type

transactions = []
# for the user to enter the amount wrapping in error handling
transaction_date = datetime.now()
# try:
#    amount = input("Enter amount: ")
#except TypeError:
#    print("Please enter valid amount")
# then store the transactions
user_transaction = Transaction(1000, transaction_date, "income")
user_transaction_2 = Transaction(200, transaction_date, "expense")
user_transaction_3 = Transaction(500, transaction_date, "income")
user_transaction_4 = Transaction(100, transaction_date, "expense")
transactions.append(user_transaction_2)
transactions.append(user_transaction_3)
transactions.append(user_transaction_4)

def log_call(func):
    def wrapper(*args, **kwargs): # means accept any argumrnt however many.
        print("calling savings")
        result = func(*args, **kwargs) # here it means unpack and forward, *args, **kwargs.
        print("savings recorded")
        return result
    return wrapper

@log_call
def savings(transactions):
    total = 0
    for t in transactions:
        if t.type == "income":
            total = total + t.amount
        else:
            total = total - t.amount
    return total

result = savings(transactions)
print(result)

if result < 500:
    print("Low on savings")
else:
    print("savings look healthy")
