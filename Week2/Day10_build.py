# Day 10 Build challenge
# here in this build we will refractor the quiz with error handling using try/except blocks
# in this function we have put in the error handling inside the file opening as this is the part that could go wrong.
# for instance someone can write wrong input and the code could carsh
def read_reviews(filename):
    clean_file = []
    try:
        with open(filename) as p:
            for f in p:
                try: # here we have added error handling for bad and misinformed data
                    read_only = f.strip()
                    clean_data = read_only.split(" | ")
                    raw_data = (clean_data[0], clean_data[1], clean_data[2]) # here building the tuple
                    clean_file.append(raw_data)
                except IndexError:
                    print(f"some bad data: {f}")
        return clean_file
    except FileNotFoundError: # to save the crash we put in a empty list that works gracefully and returns an empty list
        print("Data not found")
    return []

def main():
    filename = "pearl_reviews.txt"
    result = read_reviews(filename)
    print(result)

main()
# here we checked that if user has given a wrong input we can still gracefully handle and let the other functions 
# work instead of crashing the code    