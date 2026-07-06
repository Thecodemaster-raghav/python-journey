# find the longest common prefix in a list of strings

# in this problem the brute force solution that i can think of is that we will have a empty list
# inside of the function and will loop through the list of strings and if the 1st two chars match of th each string 
# will append it and return that and set a default empty string to return.

class Solution(object):
    def longestPrefix(self, strs):
        chars = []
        for i in strs:
            if i == strs[0][1]:
                chars.append(i[0][1])
        return chars
    
result = Solution().longestPrefix(["raghav", "ravi", "rajan"])
print(result)