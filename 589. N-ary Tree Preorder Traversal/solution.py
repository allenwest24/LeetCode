"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        out = []
        if root == None:
            return out
        out.append(root.val)
        if root.children != None:
            for c in root.children:
                out += self.preorder(c)
        return out
