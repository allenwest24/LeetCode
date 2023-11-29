# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # If you get to the end of a branch, add nothing.
        if root is None:
            return 0
        
        # Call left, call right
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        # Whichever returns bigger, return that plus one.
        return left + 1 if left > right else right + 1
