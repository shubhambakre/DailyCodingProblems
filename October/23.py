# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Amazon.
#
# A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:
#
#         4
#       / | \
#     3   5   3
#   /           \
# 9              9
# Given a k-ary tree, determine whether it is symmetric.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root,root)
    
    def isMirror(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        return (root1.val == root2.val) and self.isMirror(root1.right,root2.left) and                           self.isMirror(root1.left, root2.right)
    
