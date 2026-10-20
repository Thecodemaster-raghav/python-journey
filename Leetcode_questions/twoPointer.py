# the two pointer approach with 2 separate but sorted lists
# one loop runs checking the lists indexes and comparing them against one an other
# here in this approach i am comparing the smallest and moving only the smallest because that is safe
# .extend is for all the leftover code ffrom either of the lists to be appended inside the full list

class Solution(object):
    def towPointer(self, s, t):
        merged_list = []
        left_s = 0
        left_t = 0
        while (left_s < len(s) and left_t < len(t)):
            if s[left_s] < t[left_t]:
                left_s += 1
                continue
            if s[left_s] > t[left_t]:
                left_t += 1
                continue
            if s[left_s] == t[left_t]:
                merged_list.append(s[left_s])
                left_s += 1
                left_t += 1
                continue
        return merged_list

result = Solution().towPointer([3, 7, 12, 18, 25], [7, 9, 18, 30])
print(result)