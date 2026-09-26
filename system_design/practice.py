# the base62 algorithm for the URL shortner system design practice 
# now designing a URL shortner for CLI short script
alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def tobase(nums):
    new_list = [] # empty list to catch the chars
    while(nums>0): # do the division up until the remainder is greater than 0
        index = nums % 62 # catches the index
        rem = alphabet[index]
        nums = nums // 62 # quotient 
        new_list.append(rem) # addin the chars to the empty string
    result = "".join(new_list[::-1]) # reversing and than joining the list
    return result

class URLShortner:
    def __init__(self):
        self.counter = 0 # a counter that increases whenever the URL is hit
        self.store = {} # dict store for lookup

    def shorten(self, long_url): # method for long_url to short_url
        self.counter += 1
        short_url = tobase(self.counter) # wrapping the counter into tobase function
        self.store[short_url] = long_url
        return short_url # return the short 

    def resolve(self, short_code):
        if short_code in self.store:
            return self.store[short_code] # returning to the long form url originally pasted
        else:
            raise KeyError("Not Found")

url = URLShortner()
new_url1 = url.shorten("https://leetcode.com")
new_url2 = url.shorten("https://github.com")
print(new_url1, new_url2 )
print(url.resolve(new_url1))
print(url.resolve(new_url2))