# char count problem
# given a string of chars find the matching char and return the index and the count 

class CharString(object):
    def find_char(self, name, target):
        count = 0
        chars = []
        for n in range(len(name)):
            if name[n] == target:
                count += 1 # increment the count as the matching char is found
                chars.append(n) # append that index where the matching char was found
        return chars, count # returning both chars and count as then lets say if the char is non empty 
    # and count is < 0 so for count there is no need of a separate flagship

class Solution(object):
    def countWords(self, words):
        words_count = words.lower().split() # .lower() for normalization and .split() for splitting the string into a list 
        total = {}
        for w in words_count:
            if w in total:
                total[w] += 1
            else:
                total[w] = 1
        sorted_words = sorted(total.items(), key=lambda x: x[1], reverse=True)[:2] # to get the top 2 pairs
        return sorted_words        

result = Solution().countWords("raghav Raghav Keshav keshav taran Happy")
print(result)