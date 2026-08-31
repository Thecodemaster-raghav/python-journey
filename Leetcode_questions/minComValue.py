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