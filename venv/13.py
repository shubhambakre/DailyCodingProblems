# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Salesforce.
#
# Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.
#
# If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.
#

class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# Given a binary tree, prints nodes
# in inorder
def inorder(node):
    if (not node):
        return

    # first recur on left child
    inorder(node.left)

    # then print the data of node
    print(node.data, end = " ")

    # now recur on right child
    inorder(node.right)

# Function to merge given two
# binary trees
def MergeTrees(t1, t2):
    if (not t1):
        return t2
    if (not t2):
        return t1
    t1.data += t2.data
    t1.left = MergeTrees(t1.left, t2.left)
    t1.right = MergeTrees(t1.right, t2.right)
    return t1

# Driver code
if __name__ == '__main__':

    # Let us construct the first Binary Tree
    #     1
    #     / \
    #     2     3
    # / \     \
    # 4 5     6
    root1 = newNode(1)
    root1.left = newNode(2)
    root1.right = newNode(3)
    root1.left.left = newNode(4)
    root1.left.right = newNode(5)
    root1.right.right = newNode(6)

    # Let us construct the second Binary Tree
    #     4
    #     / \
    # 1     7
    # /     / \
    # 3     2 6
    root2 = newNode(4)
    root2.left = newNode(1)
    root2.right = newNode(7)
    root2.left.left = newNode(3)
    root2.right.left = newNode(2)
    root2.right.right = newNode(6)

    root3 = MergeTrees(root1, root2)
    print("The Merged Binary Tree is:")
    inorder(root3)
