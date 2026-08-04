class Solution(object):
    def minOfTwo(self, cost):
        # the greedy approach; buy 2 get 1 for free and it satisfies the approach of getting the 
        # most expensive you have to have the 2 highest totals and skip every third element.
        # using sorting for O(n log n) and O(n) for the loop pass
        mincost = 0
        sorted_cost = sorted(cost, reverse=True)
        for n in range(len(sorted_cost)):
            if n % 3 != 2: # every skipped element has to have a group of three but they do not satisfy that
                # condition and what is left with us is 2
                mincost += sorted_cost[n]
        return mincost

result = Solution().minOfTwo([1, 2, 3])
print(result)