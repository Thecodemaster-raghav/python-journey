# generating a netflix style piepline which netflix uses for real world editing scenarios

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
            "start": start,
            "end": end,
            "text": text
        }
        merged_blocks.append(merged)
    return merged_blocks

result = parse(blocks, "ep2")
print(result)
