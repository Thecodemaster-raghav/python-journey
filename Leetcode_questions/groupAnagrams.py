# 1: take a dict outside the loop,
# 2: inside the loop sort the words in the list and join them 
# 3: check if the key in the dict exists; if it does exists have a empty list equalled to the dicts key
# than return the dict[keys]'s values as a list.
# as sorting takes time and the loop is O(n klogk)

class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in groups:
                groups[key] = []
            groups[key].append(i)
        return list[groups.values()]

result = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)