from side_project2 import Transaction, json, transactions, datetime

# now loading the file back 
def load(file):
    with open("transaction.json", "r", encoding="utf-8") as file:
        load_file = json.load(file)
        new_transaction = []
        for r in load_file:
            new_dict = Transaction(**r)
            new_transaction.append(new_dict)
        for n in new_transaction:
            print(n.amount, n.date, n.type)

load_result = load("transaction.json")
print(load_result)