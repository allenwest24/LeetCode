# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def split(self, root):
        print("gjgj")
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # If you get to the end of a branch, add nothing.
        if root == None:
            return 0
        
        # Call left, call right
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        # Whichever returns bigger, return that plus one.
        if left > right:
            return left + 1
        else:
            return right + 1
