# char count problem
# given a string of chars find the matching char and return the index and the count 

class CharString(object):
    def find_char(self, name, target):
        count = 0
        chars = []
        for n in range(len(name)):
            if name[n] == target:
                count += 1 # increment the count as the matching char is found
                chars.append(n) # append that index where the matching char was found
        return chars, count # returning both chars and count as then lets say if the char is non empty 
    # and count is < 0 so for count there is no need of a separate flagship