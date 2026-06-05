# DAY 9 : Refactor the build from day 8

def read_reviews(filename):
    with open("pearl_reviews.txt") as g:
        reviews = []
        for i in g:
            text = i.strip()
            clean_data = text.split(" | ")
            row = (clean_data[0], clean_data[1], clean_data[2] == "True")
            reviews.append(row)
    return reviews

# here we are applytng comrehension:

def analyze(result):
    total_reviews = len(result)
    unique_pearl_set = {pearl_id for pearl_id, difficulty, was_correct in result}
    wrong_set_pearls = {pearl_id for pearl_id, difficulty, was_correct in result if was_correct == False}
    return total_reviews, unique_pearl_set, wrong_set_pearls

def main():
    total = read_reviews("pearl_reviews.txt")
    analysis = analyze(total)
    print(analysis)
main()