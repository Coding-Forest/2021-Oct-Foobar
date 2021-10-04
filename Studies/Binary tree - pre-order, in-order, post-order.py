# Pre-/In-/Post-ordre binary tree serach
# Code from LucidProgramming (2018)

class Node(object):
    def __init__(self, value): # type of value we want to store in each node.
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root) # root is a value that will be passed in to define the binary tree.

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print(f"traversal type: {str(traversal_type)} is not supported.")


    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal


tree = BinaryTree(7)
tree.root.left = Node(3)
tree.root.right = Node(6)
tree.root.left.left = Node(1)

# References:
# mycodeschool (2015) Binary tree traversal: Preorder, Inorder, Postorder https://www.youtube.com/watch?v=gm8DUJJhmY4&ab_channel=mycodeschool
# LucidProgramming (2018) Binary Trees in Python: Introduction and Traversal Algorithms https://www.youtube.com/watch?v=6oL-0TdVy28&ab_channel=LucidProgramming
