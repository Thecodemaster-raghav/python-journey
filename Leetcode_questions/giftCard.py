# scenario: customer has a $50 gift card so return the 2 indicies in the list 
# which adds up to the target number 50
# using the 2 pointer approach
# time complexity is O(n) and space complexity remains the same as the brute force solution of 2 loops with checking
# every index which is O(1)
class Solution(object):
    def getCard(self, prices, target):
        left = 0
        right = len(prices) - 1
        while (left < right):
            total = prices[left] + prices[right]
            if total < target:
                left += 1
                continue
            if total > target:
                right -= 1
                continue
            if total == target:
                return [left, right]
        return []

result = Solution().getCard([8,  12,  18,  22,  32,  35,  41], 50)
print(result)