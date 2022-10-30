# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Google.
#
# Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    max_value = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.postorder(root)
        return self.max_value
    
    def postorder(self, root: Optional[TreeNode]):
        if root == None:
            return 0
        left = max(self.postorder(root.left),0)
        right = max(self.postorder(root.right),0)
        
        self.max_value = max(self.max_value, left+right+root.val)
        return max(left,right) + root.val
    
