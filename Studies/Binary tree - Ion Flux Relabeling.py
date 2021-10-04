# Visible Logic Assurance Check

import copy

def solution(h, q):

    p = []
    height = copy.deepcopy(h)

    # for each element in p, travel down the tree using depth index 'h'.
    for i in range(len(q)):

        h = height          # at the start of each for loop, restart h to the input tree height.
        parent = 2 ** h - 1

        print(f"\nstart of loop {i +1} of {len(q)} to search for {q[i]} =============\n")
        print(f"    height refreshed to {height}\n")

        # Handle the top root case.
        # No such converter for the one sitting at the top root location.
        if q[i] == parent:
            p.append(-1)
            print("    append -1\n")

        # if not the top root,
        else:
            # search through the tree from top down until the target value is found.
            while h > 0:
                # while step 1
                # Set the parent, left and right child node values.
                h -= 1
                print(f"    while step 1) with h = {h}")
                left = parent - 2 ** h
                right = parent - 1
                print(f"        parent parent {parent}, left {left}, right {right}\n")

                # while step 2
                print(f"    while step 2) - if q[i] matches left or right")
                # if the value is found, append the parent and break out of the while, jump to the next for iteration.
                if (q[i] == left or q[i] == right):
                    p.append(parent)
                    print(f"        {q[i]} == {left} or {right}")
                    print(f"        append parent {parent}\n")
                    break

                # if the value is not found,
                else:
                    print("    while step 3) - else")
                    # update parent to the left or right node. And go back up to the while loop while h > 0.
                    if q[i] < left:
                        parent = left
                        print(f"        parent updated to {left}\n")
                    else:
                        parent = right
                        print(f"        parent updated to {right}\n")

        print(f"    result of iteration {i}: {p}\n")

        print(f"=============Iteration {i + 1} of {len(q)} completed.\n\n")

    return p

  

"""

************************************************ for solution(5, [19, 14, 28])) ************************************************
 
start of loop 1 of 3 to search for 19 =============

    height refreshed to 5

    while step 1) with h = 4
        parent parent 31, left 15, right 30

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 30

    while step 1) with h = 3
        parent parent 30, left 22, right 29

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 22

    while step 1) with h = 2
        parent parent 22, left 18, right 21

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 21

    while step 1) with h = 1
        parent parent 21, left 19, right 20

    while step 2) - if q[i] matches left or right
        19 == 19 or 20
        append parent 21

    result of iteration 0: [21]

=============Iteration 1 of 3 completed.



start of loop 2 of 3 to search for 14 =============

    height refreshed to 5

    while step 1) with h = 4
        parent parent 31, left 15, right 30

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 15

    while step 1) with h = 3
        parent parent 15, left 7, right 14

    while step 2) - if q[i] matches left or right
        14 == 7 or 14
        append parent 15

    result of iteration 1: [21, 15]

=============Iteration 2 of 3 completed.



start of loop 3 of 3 to search for 28 =============

    height refreshed to 5

    while step 1) with h = 4
        parent parent 31, left 15, right 30

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 30

    while step 1) with h = 3
        parent parent 30, left 22, right 29

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 29

    while step 1) with h = 2
        parent parent 29, left 25, right 28

    while step 2) - if q[i] matches left or right
        28 == 25 or 28
        append parent 29

    result of iteration 2: [21, 15, 29]

=============Iteration 3 of 3 completed.


final answer: [21, 15, 29]




************************************************ for solution(3, [7, 3, 5, 1]) ************************************************


start of loop 1 of 4 to search for 7 =============

    height refreshed to 3

    append -1

    result of iteration 0: [-1]

=============Iteration 1 of 4 completed.



start of loop 2 of 4 to search for 3 =============

    height refreshed to 3

    while step 1) with h = 2
        parent parent 7, left 3, right 6

    while step 2) - if q[i] matches left or right
        3 == 3 or 6
        append parent 7

    result of iteration 1: [-1, 7]

=============Iteration 2 of 4 completed.



start of loop 3 of 4 to search for 5 =============

    height refreshed to 3

    while step 1) with h = 2
        parent parent 7, left 3, right 6

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 6

    while step 1) with h = 1
        parent parent 6, left 4, right 5

    while step 2) - if q[i] matches left or right
        5 == 4 or 5
        append parent 6

    result of iteration 2: [-1, 7, 6]

=============Iteration 3 of 4 completed.



start of loop 4 of 4 to search for 1 =============

    height refreshed to 3

    while step 1) with h = 2
        parent parent 7, left 3, right 6

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 3

    while step 1) with h = 1
        parent parent 3, left 1, right 2

    while step 2) - if q[i] matches left or right
        1 == 1 or 2
        append parent 3

    result of iteration 3: [-1, 7, 6, 3]

=============Iteration 4 of 4 completed.


final answer: [-1, 7, 6, 3]






************************************************ for solution(3, [1, 4, 7]) ************************************************

start of loop 1 of 3 to search for 1 =============

    height refreshed to 3

    while step 1) with h = 2
        parent parent 7, left 3, right 6

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 3

    while step 1) with h = 1
        parent parent 3, left 1, right 2

    while step 2) - if q[i] matches left or right
        1 == 1 or 2
        append parent 3

    result of iteration 0: [3]

=============Iteration 1 of 3 completed.



start of loop 2 of 3 to search for 4 =============

    height refreshed to 3

    while step 1) with h = 2
        parent parent 7, left 3, right 6

    while step 2) - if q[i] matches left or right
    while step 3) - else
        parent updated to 6

    while step 1) with h = 1
        parent parent 6, left 4, right 5

    while step 2) - if q[i] matches left or right
        4 == 4 or 5
        append parent 6

    result of iteration 1: [3, 6]

=============Iteration 2 of 3 completed.



start of loop 3 of 3 to search for 7 =============

    height refreshed to 3

    append -1

    result of iteration 2: [3, 6, -1]

=============Iteration 3 of 3 completed.


final answer: [3, 6, -1]

Process finished with exit code 0

"""
