# key algorithm: indexing with two index variables i & j 

import numpy as np 

def answer(I, t):
    
    sub_list = []
    sum = 0                              # compare against the target integer t

    for i in range(len(I)):              # start index
        for j in range(i+1, len(I)+1):   # end index. initial j should be always greater than initial i by 1. 
            sum = np.sum(I[i: j])

            if sum == t:
                sub_list = [i, j-1]
                return sub_list          # if found the match, return the index list and break out of the code.
            else: continue               # continue the nested for loop until the desired indexing is found.

    if sub_list == []:                   # Final check: if indexing is not found, 
        sub_list = [-1, -1]              # return the null case index. 
    return sub_list 
        

I = [4, 3, 5, 7, 8]
t = 12

print(answer(I, t))
print(answer([1, 2, 3, 4], 15))

print(answer([4, 3, 10, 2, 8], 12))
print(answer([1, 3, 6, 2, 2], 4))
print(answer([3, 9, 5, 3, 0], 3))
print(answer([3, 5, 1, 4, 2], 12))
print(answer([1, 0, 0, 0, 1, 0, 1], 2))
