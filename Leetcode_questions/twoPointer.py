# the two pointer approach with 2 separate but sorted lists
# one loop runs checking the lists indexes and comparing them against one an other
# here in this approach i am comparing the smallest and moving only the smallest because that is safe

class Solution(object):
    def towPointer(self, s, t):
        new_list = []
        left_s = 0
        left_t = 0
        while (left_s < len(s) and left_t < len(t)):
            if s[left_s] < t[left_t]:
                new_list.append(s[left_s])
                left_s += 1
                continue
            if s[left_s] > t[left_t]:
                new_list.append(t[left_t])
                left_t += 1
                continue
            if s[left_s] == t[left_t]:
                new_list.append(s[left_s])
                left_s += 1
                continue
        new_list.extend(s[left_s:])
        new_list.extend(t[left_t:])
        return new_list

result = Solution().towPointer([9, 11, 14], [10, 12, 13, 16])
print(result)