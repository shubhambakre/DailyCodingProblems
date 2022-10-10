# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# Given a node in a binary search tree, return the next bigger element, also known as the inorder successor.
#
# For example, the inorder successor of 22 is 30.
#
#    10
#   /  \
#  5    30
#      /  \
#    22    35
# You can assume each node has a parent pointer.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        if p.right is not None:
            return self.minValue(p.right)

        succ = TreeNode("null")

        while(root):
            if(root.val < p.val):
                root = root.right
            elif(root.val > p.val):
                succ = root
                root = root.left
            else:
                break
        return succ

    def minValue(self,node):

        current = node

        while(current is not None):
            if current.left is None:
                break
            current = current.left
        return current

