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
