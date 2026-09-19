# the base62 algorithm for the URL shortner system design practice 
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def to_base(number) -> int:
    new_chars = []
    while(number > 0): # dividing the numbers and the remainder is less than 0
        index = number % 62 # deving and getting the index
        remainder = alphabet[index] # to get the chars
        new_chars.append(remainder) # addin those chars to the empty list
        number = number // 62
    new_nums = "".join(new_chars[::-1]) # having the list of chars and ::-1 returns a reversed list
    return new_nums

result = to_base(262)
print(result)