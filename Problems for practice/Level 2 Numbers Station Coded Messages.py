import numpy as np 

def answer(I, t):
    
    sub_list = []
    sum = 0
    
    for i in range(len(I)):
        for j in range(i+1, len(I)+1):
            sum = np.sum(I[i: j])

            if sum == t:
                sub_list = [i, j-1]
                return sub_list 
            else: continue

    if sub_list == []:
        sub_list = [-1, -1]
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
