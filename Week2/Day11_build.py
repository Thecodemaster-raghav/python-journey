# building the musle to split our pearl review analyzer to logical modules
# here is the main file that jots them all together all the other modules
import readers, analyzer, reporter
def main():
    all_reviews = readers.read_reviews("pearl_reviews.txt")
    analysis = analyzer.analyze(all_reviews)
    reporter.write_report(analysis, "report.txt")

if __name__ == "__main__":
    main() # the gaurd that if anyone ever imports main it never runs the whole import