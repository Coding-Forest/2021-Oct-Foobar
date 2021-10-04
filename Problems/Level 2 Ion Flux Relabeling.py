import copy

def solution(h, q):

    p = []
    height = copy.deepcopy(h)

    # for each element in p, travel down the tree using depth index 'h'.
    for i in range(len(q)):

        h = height          # at the start of each for loop, restart h to the input tree height.
        parent = 2 ** h - 1

        # Handle the top root case.
        # No such converter for the one sitting at the top root location.
        if q[i] == parent:
            p.append(-1)

        # if not the top root,
        else:
            # search through the tree from top down until the target value is found.
            while h > 0:
                # Set the parent, left and right child node values.
                h -= 1
                left = parent - 2 ** h
                right = parent - 1

                # if the value is found, append the parent and break out of the while, jump to the next for iteration.
                if (q[i] == left or q[i] == right):
                    p.append(parent)
                    break

                # if the value is not found,
                else:
                    # update parent to the left or right node. And go back up to the while loop while h > 0.
                    if q[i] < left:
                        parent = left
                    else:
                        parent = right

    return p
  
  
  
"""
Visible logic assurance code is the separate folder Studies.
"""

# Without notes
def solution(h, q):

    p = []
    height = copy.deepcopy(h)

    for i in range(len(q)):

        h = height          
        parent = 2 ** h - 1
        
        if q[i] == parent:
            p.append(-1)
            
        else:
            while h > 0:
                h -= 1
                left = parent - 2 ** h
                right = parent - 1

                if (q[i] == left or q[i] == right):
                    p.append(parent)
                    break

                else:
                    if q[i] < left:
                        parent = left
                    else:
                        parent = right

    return p
 
    
