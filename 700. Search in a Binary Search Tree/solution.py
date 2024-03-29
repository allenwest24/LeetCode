# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val == val:
            return root
        if root.left:
            lans = self.searchBST(root.left, val)
            if lans != None:
                return lans
        if root.right:
            rans = self.searchBST(root.right, val)
            if rans != None:
                return rans
        if not root.right and not root.left:
            return None
            
