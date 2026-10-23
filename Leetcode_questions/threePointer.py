# a three pointer problem which involves writes 

class Solution(object):
    def threePointer(self, nums):
        left = 0
        right = len(nums) - 1
        output = [0] * len(nums)
        write = len(output) - 1
        while (left <= right):
            squared_left = nums[left] ** 2
            squared_right = nums[right] ** 2
            if squared_left < squared_right:
                right -= 1
                output[write] = squared_right
                write -= 1
                continue
            if squared_left >= squared_right:
                left += 1
                output[write] = squared_left
                write -= 1
                continue
        return output

result = Solution().threePointer([-7, -3, 2, 3, 11])
print(result)
