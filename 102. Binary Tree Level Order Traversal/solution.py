# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        out = []
        if root == None: return out
        curr_level = [root]
        while curr_level:
            curr_nodes = []
            next_level = []
            for node in curr_level:
                curr_nodes.append(node.val)
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            out.append(curr_nodes)
            curr_level = next_level
            
        return out
