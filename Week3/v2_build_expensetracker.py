from side_project2 import Transaction, json, transactions, datetime

# now loading the file back 
def load(file):
    with open("transaction.json", "r", encoding="utf-8") as file:
        load_transaction = json.load(file)
        new_transactions = []
        for i in load_transaction: # this loop makes the json file as dicts
            now_total = Transaction(**i) # **i lets us unpack json keywords into arguments
            new_transactions.append(now_total)
        for r in new_transactions:
            print(r.amount, r.date, r.type)

result = load("transaction.json")
print(result)
