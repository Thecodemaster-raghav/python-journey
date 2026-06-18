# Palindrome number
class Solution(object):
    def isPalindrome(self, x):
        num = str(x) # conveted it to a string first 
        num2 = num[::-1] # used slicing to reverse the string
        if num == num2:
            return True
        else:
            return False

result = Solution().isPalindrome(121)
print(result)

# Two sum: using lists dicts and loops
class Solution(object):
    def two_sum(self, nums, target):
        self.nums = list(nums)
        self.target = int(target)
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                if i != j:
                    total = self.nums[i] + self.nums[j]
                    if total == self.target:
                        return i, j
    
result_twosum = Solution().two_sum([1, 2, 3, 4], 8)
print(result_twosum)
