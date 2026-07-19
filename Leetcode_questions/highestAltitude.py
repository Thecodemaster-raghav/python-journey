class Solution(object):
    def largestAltitude(self, gain):
        current = 0 # the starting point of the cyclist
        highest = 0
        for i in gain: # counting the number of times cyclist gained the altitude
            current += i # the new starting point becomes the current point and it is like catching the running total 
            # so we add the gains into the current point to make that the new point of the cyclist
            if current > highest:
                highest = current
        return highest


result = Solution().largestAltitude([-4,-3,-2,-1,4,3,2])
print(result)