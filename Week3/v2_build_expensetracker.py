from side_project2 import Transaction, json, transactions, datetime

# now loading the file back 
def load(file):
    with open("transaction.json", "r", encoding="utf-8") as file:
        load_transaction = json.load(file)
        new_transaction = []
        for i in load_transaction: # to make json file as dicts
            new_data = Transaction(**i) # lets us unpack json to python args
            new_transaction.append(new_data)
        for r in new_transaction:
            return r.amount, r.type, r.date

result = load("transaction.json")
print(result)
