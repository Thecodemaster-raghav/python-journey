class Solution(object):
    def largestAltitude(self, gain):
        current = 0 # the starting point of the cyclist
        highest = 0
        for i in gain: # counting the number of times cyclist gained the altitude
            current += i # the new starting point becomes the current point and it is like catching the running total 
            # so we add the gains into the current point to make that the new point of the cyclist
            if current > highest:
                highest = current
        return highest # returning highest unintended. as that is the edge case of what if there is a negative sum 
    # and that was the requirement which meant if the sum is not greater than 0 return 0

# the pattern = two variables walking one list - running total + track the max in one walk
# one half of that pattern lives inside of the post body which is the biggest loop and the other half lives inside my 
# pearl analyzer where we are catching the running total

# the ETL term for the value that accumulates as we walk the data - Aggregation
# the other edge case where the list is empty. than the return should be 0 because the start counts


result = Solution().largestAltitude([-4,-3,-2,-1,4,3,2])
print(result)