class Solution(object):
    def largestAltitude(self, gain):
        starting = 0
        highest = 0
        for i in gain:
            starting += i # to catch the running total
            if starting > highest: # this means that if -5 + 0 = -5 which is less than that of 0 and all of those values are discarded. which are less than 0 and in our case only 1 was greater than 0 which was 1 and that is what we returned. traced on paper first
                highest = starting
        return highest

result = Solution().largestAltitude([-5,1,5,0,-7])
print(result)