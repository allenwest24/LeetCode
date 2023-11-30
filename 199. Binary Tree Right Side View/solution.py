# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Base case
        if not root:
            return []

        # Create a shared list that will be our output
        out = []

        # Create a function that will append the current node if one has not been done yet
        # then make sure to always go right to check for a valid addition before going left. 
        def appendIfRight(curr_root, level):
            if curr_root:
                if len(out) == level:
                    out.append(curr_root.val)
                appendIfRight(curr_root.right, level + 1)
                appendIfRight(curr_root.left, level + 1)

        # Call and return outcome
        appendIfRight(root, 0)
        return out
        
