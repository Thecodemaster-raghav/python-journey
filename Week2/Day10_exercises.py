# Day 10 exercises.
# convert with failures
raw = ["12", "5", "hello", "8", "abc", "20"]

expected_int = []
for r in raw:
    try:
        num = int(r)
        expected_int.append(num) # appending the int values
    except:
        print(f"Skip Invalid value: {r}") # here we skipped the values which are not int
print(expected_int)

# Exercise 2: Validate records, skip the broken ones
user = [
    {"name": "alice", "age": 30},
    {"name": "bob"},
    {"name": "charlie", "age": 45},
    {"age": 40},
]
# building the list of names of users whose names are above 18 years
input_user = []
for u in user:
    try: 
        if u["age"] > 18:
            input_user.append(u["name"])
    except KeyError:
        print(f"Invalid input: {u}") # collects the data which is missing and or broken
print(input_user)

# Raise your own validation and catch it.
scores = [85, 120, 60, -5, 95]
def validate_score(scores):
    if scores < 0 or scores > 100:
        raise ValueError("Score out of range") # raises an error
    return scores

valid_scores = [] # here the scores that are within bounds gets passed

for score in scores:
    try:
        valid_scores.append(validate_score(score)) # here had to pass the function inside the append to get the values from the 
        #above function
    except:
        print(f"List out of bounds: {score}")
print(valid_scores)

# Nested dicts access with failures:
records = [
    {"user": {"name": "alice", "email": "alice@mail.com"}},
    {"user": {"name": "bob"}},
    {"user": {"name": "charlie", "email": "chalie@mail.com"}},
    {"account": "broken"},
]

emails_lists = []
for r in records:
    try:
        emails_lists.append(r["user"]["email"]) # appended the list of emails just loop no if block
    except KeyError:
        print(f"Missing or broken data: {r}") # gives us the kipped values
print(emails_lists)

# Convert and filter in one pass:
raw_prices = ["19.99", "free", "45.00", "N/A", "12.50", ""]
prices_after_review = []
for clean in raw_prices: # in this exercise the order matters as we need to have the conversion inside of the try block not outside
    try:
        numbers = float(clean)
        if numbers > 15.00:
            prices_after_review.append(numbers)
    except ValueError:
        print(f"Invalid prices: {clean}")
print(prices_after_review)

# count successes and failures 
raw_prices = ["19.99", "free", "45.00", "N/A", "12.50", ""]
count_success = 0
count_failed = 0
for p in raw_prices:
    try:
        n = float(p)
        count_success = count_success + 1
    except:
        count_failed = count_failed + 1
        print(f"Failed count: {p}")
print(count_success)
print(count_failed)