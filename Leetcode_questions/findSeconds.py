# two lists of he and how find the seconds where both the words were spoken at the same time



def findSeconds(hey, how):
    new_list = []
    i = 0
    j = 0
    while(i<len(hey) and j<len(how)):
            if hey[i] < how[j]:
                i += 1
            elif hey[i] == how[j]:
                new_list.append(hey[i])
                i+=1
                j+=1
            else:
                 j+=1
    return new_list 
                
result = findSeconds([1, 2], [5, 6])
print(result)