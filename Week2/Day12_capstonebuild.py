# PEARL ANALYZER CAPSTONE
# Things to check first 
# we will build 3 classes before we were working with raw tuples now we will be working with
# OOPS concepts with 3 classes and all the classes having there own methods and objects to call upon

# Firstly the pearl class should hold an attribute called perarl_id. As we want pearl ID's
# secondly yes our pearls should know where it needs reviews that method would check the questions that were wrong
# we will use inheritance for that
# Thrid: Design - yes we will need a container to check how many reviews were there like total pearls
# and then the method also checks for the difficulty but that is the inheritance part taht we will build.

class Pearl:
    def __init__(self, pearl_id, difficulty, was_correct):
        self.pearl_id =pearl_id
        self.difficulty = difficulty
        self.was_correct = was_correct

    def needs_review(self):
        return self.was_correct == False
    
class PearlAnalyzer:
    def __init__(self):
        self.pearls = []

    def add_pearls(self, check):
        self.pearls.append(check)

    def analysis_pearl(self):
        total_pearls_analyzed = len(self.pearls)
        count_reviews = 0
        for s in self.pearls:
            if s.needs_review():
                count_reviews += 1
        return f"Total pearls: {total_pearls_analyzed}, {count_reviews} needs review"
    
p1 = Pearl("p1", "Hard", False)
p2 = Pearl("p2", "Easy", True)
p3 = Pearl("p3", "Good", False)
p4 = Pearl("p4", "Again", True)
p5 = Pearl("p5", "Hard", False)
my_analyzer = PearlAnalyzer()
my_analyzer.add_pearls(p1)
my_analyzer.add_pearls(p2)
my_analyzer.add_pearls(p3)
my_analyzer.add_pearls(p4)
my_analyzer.add_pearls(p5)
print(my_analyzer.analysis_pearl())