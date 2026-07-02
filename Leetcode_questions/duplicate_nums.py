# Contains duplicate: given of list of ints find the one which is a duplicate
class Solution(object):
    def contains_duplicate(self, numbers):
        for n in range(len(numbers)):
            for i in range(len(numbers)):
                if n != i and numbers[n] == numbers[i]:
                    return True
        return False  # return early on success return default after the loop

now_result = Solution().contains_duplicate([1, 2, 4, 3])
print(now_result)

# comparing the positions as well as numbers in the brute force solution.

# solution using set data structures as it eliminates duplicates
class Solution(object):
    def isDuplicate(self, nums):
        check = set()
        for n in nums:
            if n in check: # to check if there is a duplicate inside of the list using a set
                return True
            else:
                check.add(n) # to add the values which do not match inside of the set
        return False

new_result = Solution().isDuplicate([1, 5, 6, 8])
print(new_result)