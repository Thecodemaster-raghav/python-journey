# find the longest common prefix in a list of strings

# in this problem the brute force solution that i can think of is that we will have to march through positions and
# match the chars at those positions with the next chars at same 1st two positions and will need to have a running 
# empty string that collects the matching chars and if the chars does not match it returns an empty string.

class Solution(object):
    def longestPrefix(self, strs):
        prefix = "" 
        # now the edge case as the prefix should return the for the shortest word and if not it will give an indexerror
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for w in strs:
                if w[i] != strs[0][i]:
                    return prefix
            prefix += shortest[i]
        return prefix
    
result = Solution().longestPrefix(["flower", "flight", "flow"])
print(result)

# the main crux: for each position check every word; if the instant one disagrees, stop return what we've built;
# if they all agree keep the chars and move to the next position 