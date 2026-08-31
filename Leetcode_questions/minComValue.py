class Solution(object):
    def getCommon(self, nums1, nums2):
        # the 2 pointer approach, and the lists being in bounds 
        i = 0
        j = 0
        # the out of bounds len condition
        while(i < len(nums1) and j < len(nums2)):
            # return smallest if equal
            if nums1[i] == nums2[j]:
                return nums1[i]
            # if the nums1[i] is smaller then advance
            elif nums1[i] < nums2[j]:
                i += 1
            # else advance j
            else: 
                j += 1
        return -1

result = Solution.getCommon([1,2,3], [2,4])
print(result)

# the approach with set 
# using set and the sorted list will give the smallest value
# put 1 list inside set and traverse the other with a for loop return n if similar and return -1 if not

class Sol(object):
    def comValue(self, nums1, nums2):
        nums = set(nums1)
        for n in nums2:
            if n in nums:
                return n
        return -1

result1 = Sol().comValue([1,2,3,6], [2,3,4,5])