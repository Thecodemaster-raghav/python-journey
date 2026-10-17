# step1 is creating an empty list
# step 2 is looping over the string 
# step 3 is the gatekeeper which means if string is cleaned than only store the 
# lowercase chars into the empty list and than compare using slicing ::-1

class Solution(object):
    def isPalindrome(self, s):
        cleaned = []
        for i in s:
            if i.isalnum():
                cleaned.append(i.lower())
        return cleaned == cleaned[::-1]

result = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(result)