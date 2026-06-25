# function that reads a file updates and counts 
def read_file(practicefile):
    count = {}
    total = 0
    with open("sample.txt") as f:
        for i in f:
            data = i.split()
            category = data[0]
            amount = data[1]
            total = total + int(amount)
            count[category] = int(amount)
    return total, count

def print_reports(total, count):
    print(f"Total amount: {total}")
    for k, v in count.items():
        print(f"{k}: {v}")

def main():
    total, count = read_file("sample.txt")
    print_reports(total, count)

main()