# generating a netflix style piepline which netflix uses for real world editing scenarios
from decimal import Decimal

# open the sample data
def read_sample(subtitles):
    with open(subtitles, "r") as sample_data:
        encoded_data = sample_data.read()
        new_string_file = encoded_data.split("\n\n")
        return new_string_file
blocks = read_sample("sample.srt")

def convert_secs(time):
    hours, minutes, leftover = time.split(":")
    seconds, miliseconds = leftover.split(",")
    total = int(hours) * 3600 + int(minutes) * 60 + int(seconds) + int(miliseconds) / 1000
    return total

def parse(blocks, video_id):
    merged_blocks = []
    for r in blocks:
        new_blocks = r.split("\n")
        start, end = new_blocks[1].split(" --> ")
        text = "".join(new_blocks[2:])
        merged = {
            "video_id": video_id,
            "start": convert_secs(start),
            "end": convert_secs(end),
            "text": text
        }
        merged_blocks.append(merged)
    return merged_blocks

# passing the row and time of silences 
rows = parse(blocks, "ep1")
time_in_secs = 0.3
def find_silences(rows, time_in_secs):
    threshold = []
    for i in range(1, len(rows)):
        if rows[i]["start"] - rows[i - 1]["end"] < time_in_secs:
            continue
        else:
            threshold.append((rows[i-1]["end"], rows[i]["start"]))
    return threshold

# function for counting all the words inside rows

def count_words(rows):
    total_words = 0
    for i in rows:
        words = i["text"].split()
        total_words += len(words)
    return total_words


# function to return the whole dict which runs the longest
def longest_line(rows):
    best = rows[0]
    for r in range(len(rows)):
        new = rows[r]["end"] - rows[r]["start"]
        longest_run = best["end"] - best["start"]
        if new > longest_run:
            best = rows[r]
    return best

# find the matching word in the text
def find_texts(rows, text):
    searched_list = []
    for r in range(len(rows)):
        if text.lower() in rows[r]["text"].lower():
            searched_list.append(rows[r])
    return searched_list

# converting data into 1 second buckets
def convert_to_buckets(rows):
    buckets = {}
    for r in range(len(rows)):
        first = int(rows[r]["start"])
        # handling the edge case for 5.0 and 5
        if rows[r]["end"] == int(rows[r]["end"]):
            last = int(rows[r]["end"]) - 1
        else:
            last = int(rows[r]["end"])
        for seconds in range(first, last + 1):
            key = (rows[r]["video_id"], seconds)
            if key not in buckets:
                buckets[key] = []
            buckets[key].append(rows[r]["text"])
    return buckets

# building the index search for finding the words matching with the buckets they fall into
buckets=convert_to_buckets(rows)
def find_index(buckets):
    indexes = {}
    for keys, texts in buckets.items():
        for text in texts:
            for words in text.lower().split():
                if words not in indexes:
                    indexes[words] = []
                if keys not in indexes[words]:
                    indexes[words].append(keys)
    return indexes

# getting the start point of every sentence from rows

def build_index_rows(rows):
    index = {}
    for row in rows:
        text = row["text"]
        entry = (row["video_id"], row["start"])
        words = text.lower().split()
        for word in words:
            if word not in index :
                index[word] = []
            if not index[word] or entry != index[word][-1]:
                index[word].append(entry)
    return index

# adding the search layer on top of the rows
# in dicts .get(key, default) gives out the default instead of crashing 
index = build_index_rows(rows)
def search(index, word):
    # here left [] as default so that nothing crashes and a [] list comes as output 
    return index.get(word, []) 