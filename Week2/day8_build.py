# Day 8 build challenge. Pearl-Review-Analyzer

def read_reviews(filename):
    reviews = []
    with open(filename) as f:
        for i in f:
            text = i.strip()
            clean_data = text.split(" | ")
            row = (clean_data[0], clean_data[1], clean_data[2] == "True")
            reviews.append(row)
    return reviews

def analyze(result):
    total_reviews = len(result)
    unique_pearls_set = set()
    wrong_set_pearls = set()
    count = {}
    for pearls_id, difficulty, was_correct in result:
        unique_pearls_set.add(pearls_id)
        if was_correct == False:
            wrong_set_pearls.add(pearls_id)
        if difficulty in count:
             count[difficulty] = count[difficulty] + 1
        else: 
            count[difficulty] = 1
    return total_reviews, unique_pearls_set, wrong_set_pearls, count


def write_report(result, filename):
    total, unique_set, wrong_set, breakdown = result
    with open(filename, "w") as g:
        g.write("Pearl Review Report\n")
        g.write(f"Total reviews: {total}\n")
        g.write(f"Unique pearl reviews: {len(unique_set)}\n")
        g.write(f"Pearls needing review (wrong at least once): {wrong_set}\n")
        g.write(f"Difficulty breakdown: \n")
        for k, v in breakdown.items():
            g.write(f"  {k}: {v}\n")

def main():
    all_reviews = read_reviews("pearl_reviews.txt")
    analysis = analyze(all_reviews)
    write_report(analysis, "pearl_report.txt")

main()


        
    




    
