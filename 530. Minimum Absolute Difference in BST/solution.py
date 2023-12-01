# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # Base case is actually 2 nodes. 

        # Make a helper method
        def inOrderTraverse(curr_root):
            # Keep track of the semi-global variables
            nonlocal prev, best

            # Check to see if this is the end or not
            if curr_root:
                # Traverse left
                inOrderTraverse(curr_root.left)

                # Before traversing right, check the cur best value, so that we do them one at a time
                # and don't mess up the semi-global vars.
                if prev is not None:
                    best = min(best, abs(curr_root.val - prev.val))
                # Update the prev
                prev = curr_root

                # Now that we went left, we go right, with the updates semi-global vars.
                inOrderTraverse(curr_root.right)
  
        # Initialize vars and run recursive helper.
        prev = None
        best = float('inf')
        inOrderTraverse(root)
        return best
