class Solution(object):
    def reawrite(self, nums):
        read = 1
        write = 0
        while (read < len(nums)):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]
                continue
            else:
                read += 1
                continue
        return write + 1 

result = Solution().reawrite([3, 3, 7, 9, 9, 9, 12])
print(result)