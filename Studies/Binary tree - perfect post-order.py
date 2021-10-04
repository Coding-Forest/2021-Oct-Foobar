"""
# Perfect Binary Tree (PBT) 

# Description 
Let's assume that there is a perfect binary tree of a certain height. 
The leaves of the tree has a linear value of incrementing positive integers starting from one. 
Each node is filled with an integer in the order of post-order traversal. 

For instance, if we have a PBT of depth 3, the tree will look like:

     7
  3    6
1  2  4  5


## Interesting properties of PBT 
1) Relationship between the parent and right-child nodes.
In this arrangement (post-order traversal of a PBT),
the parent node of the right child node is always +1. In other words,
the right child node of the parent node is always -1. 
This is because the right node is always the last one to be visited and we have to move up the depth. 

-------------------------------------------
"
