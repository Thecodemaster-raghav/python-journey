# two sum question with brute force approach and O(n^2) time complexity

class Solution(object):
    def twoSum(self, nums, target) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i, j]

result = Solution().twoSum([2, 7, 11, 15], 26)
print(result)