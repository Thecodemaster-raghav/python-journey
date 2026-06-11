# this module takes the transforming of the data part for the pipeline.

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
