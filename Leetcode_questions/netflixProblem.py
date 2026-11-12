# a netflix article style problem where have the outut of the list as the nearest 
# second and sppend them and return 

class Solution(object):
    def netflixProblem(self, seconds):
        start = seconds[0]
        new_list = []
        for i in range(1, len(seconds)):
            # the current second equals the previous second, plus 1
            if seconds[i] == seconds[i - 1] + 1:
                continue
            else:
                new_list.append([start, seconds[i-1]])
                start = seconds[i]
        new_list.append([start, seconds[-1]])
        return new_list

result = Solution().netflixProblem([13, 14, 15, 41, 42, 90])
print(result)