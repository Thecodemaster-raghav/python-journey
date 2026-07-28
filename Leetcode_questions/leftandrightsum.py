class Solution(object):
    def LeftRightSum(self, nums):
        # brute force solution
        answer = []
        leftsum = []
        rightsum = []
        for n in range(len(nums)):
            left = sum(nums[:n]) # using the slicing operations to calculate the sum of the elements to the left of index 0 and include 
            # index 0
            leftsum.append(left)
            right = sum(nums[n+1:]) # slicing for having the sum to the right of the index 0 and not include index 0
            rightsum.append(right)
            leftright = abs(left - right) # we do not need lists we need numbers to subtract and their absolute values 
            # not their negatives so used the python built in type absolute
            answer.append(leftright)
        return answer

result = Solution().LeftRightSum([10, 4, 8, 3])
print(result)

# now the o(n) version
class newSum(object):
    def getleftRight(self, nums):
        lefts = 0
        rights = sum(nums)
        leftSum = []
        rightSum = []
        answers = []
        for n in range(len(nums)):
            leftSum.append(lefts)
            rights -= nums[n]
            rightSum.append(rights)
            nowBoth = abs(lefts - rights)
            lefts += nums[n] # we have shifted the left side operation down below as we need 
            # both the rights and lefts to be in the same state to get the required list
            answers.append(nowBoth)
        return answers

new_result = newSum().getleftRight([10, 4, 8, 3])
print(new_result)