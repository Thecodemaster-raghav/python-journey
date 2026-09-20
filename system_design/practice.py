# the base62 algorithm for the URL shortner system design practice 
class Model(object):
    def tobase(self, alphabet, nums):
        new_list = [] # empty list to catch the chars
        while(nums>0): # do the division up until the remainder is greater than 0
            index = nums % 62 # catches the index
            rem = alphabet[index]
            nums = nums // 62 # quotient 
            new_list.append(rem) # addin the chars to the empty string
        result = "".join(new_list[::-1]) # reversing and than joining the list
        return result

calc_result = Model().tobase("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", 125)
print(calc_result)
