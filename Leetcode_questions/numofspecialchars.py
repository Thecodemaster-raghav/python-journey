import string

class Solution(object):
    def numofspecialchars(self, word):
        count = 0
        words = set(word) # remove duplicates
        for i in string.ascii_lowercase: # counting each letter once
            if i.lower() in words and i.upper() in words:
                count += 1
        return count

result = Solution().numofspecialchars("aaAbcBC")
print(result)