# Day 8 build challenge. Pearl-Revoew-Analyzer


def read_reviews(filename):
    reviews = []
    with open("pearl_reviews.txt") as f:
        for i in f:
            text = i.strip()
            clean_data = text.split(" | ")
            row = (clean_data[0], clean_data[1], clean_data[2] == "True")
            reviews.append(row)
    return reviews

result = read_reviews("pearl_reviews.txt")
print(result)

def analyze(reviews):
    total_reviews = len(int("pearl_review.txt"))    
    unique_pearls_set = set()
    
