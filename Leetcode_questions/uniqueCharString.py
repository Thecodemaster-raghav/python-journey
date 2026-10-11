# steps to write the algorithm plain english
# 1. empty dict
# 2. pass 1: count every char
# 3. pass 2: for each index, left to right
#           count == 1? → return the index
# 4. loop finished, nothing found → return -1

class Solution(object):
    def firstuniqchar(self, s):
        count_chars = {}
        for i in s:
            if i in count_chars:
                count_chars[i] += 1
            else:
                count_chars[i] = 1
        for j in range(len(s)):
            if count_chars[s[j]] == 1:
                return j
        return -1

result = Solution().firstuniqchar("leetcode")
print(result)

# time complexity for the dict lookup is 0(1) for hasing and 0(n) for the loop traversal