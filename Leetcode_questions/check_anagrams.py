class Solution(object):
    def isAnagram(self, s, t):
        # if lengths differ return false (gaurd)
        # loop s seen before: increment the count or keep it 1 by default
        # same loop for t
        # last step is compare the counts and return
        # code handles all the unicode chars as well and if the input could mix forms; normalize it first
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for i in s:
            if i in count_s:
                count_s[i] += 1
            else:
                count_s[i] = 1
        for j in t:
            if j in count_t:
                count_t[j] += 1
            else:
                count_t[j] = 1
        return count_s == count_t

result = Solution().isAnagram("cat", "car")
print(result)