# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        # Val Merge
        if t1 == None and t2 == None:
            return t1
        elif t1 == None:
            t1 = t2
        elif t2 == None:
            return t1
        else:
            t1.val += t2.val
        
        # Left merge
        if t1.left == None:
            t1.left = t2.left
        elif t2.left != None:
            t1.left = self.mergeTrees(t1.left, t2.left)
        # Right Merge
        if t1.right == None:
            t1.right = t2.right
        elif t2.right != None:
            t1.right = self.mergeTrees(t1.right, t2.right)
        
        return t1
