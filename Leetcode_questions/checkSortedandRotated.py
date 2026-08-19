class Solution(object): 
    def checkRotatedSorted(self, nums):
        count = 0
        for n in range(len(nums)): # check for the rotate list and the break points
            if nums[n] == nums[(n+1) % len(nums)]:
                count+=1
        if count <= 1: # checking the break points and if count is less than or equal to 1
            # that means our list is sorted and roated and if more than 1 means not sorted or rotated
            return True
        else:
            return False

result = Solution().checkRotatedSorted([3,4,5,1,2])
print(result) 