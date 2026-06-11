# here this module will hold the data reading and cleaning part with error handling
def read_reviews(filename):
    clean_file = []
    try:
        with open(filename) as p:
            for f in p:
                try: # here we have added error handling for bad and misinformed data that is why inside the loop
                    read_only = f.strip()
                    clean_data = read_only.split(" | ")
                    raw_data = (clean_data[0], clean_data[1], clean_data[2]) # here building the tuple
                    clean_file.append(raw_data)
                except IndexError: # to catch that bad data
                    print(f"Some bad data: {f}")
        return clean_file
    except FileNotFoundError: # to save the crash we put in a empty list that works gracefully and returns an empty list
        print("Data not found")
    return []

