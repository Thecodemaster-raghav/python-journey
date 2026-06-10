# task to import this file where i need it it is concept 4 for our day 11
def doubled(number):
    num = number * number
    return num

def main():
    number = int(input())
    result = doubled(number)
    print(result)
if __name__ == "__main__":
    main() # so doing it this way the import will run the function silently and kill the ask for second input 
    # and it will kill that problem at its root.