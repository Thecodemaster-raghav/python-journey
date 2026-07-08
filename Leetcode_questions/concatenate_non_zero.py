# concatinate non zeros brute force solution
class Solution(object):
    def sumAndMultiply(self, n):
        x = str(n)
        data = [] # empty list to catch the values 
        # a running total
        total = 0
        for i in x:
            if i != '0':
                total += int(i)
                data.append(i)
        if data == []:
            return 0
        new_data = "".join(data) # to concatenate the strings which we used in the loop above
        new_total = int(new_data)
        result = total * new_total
        return result

new_result = Solution().sumAndMultiply(100030004000)
print(new_result)