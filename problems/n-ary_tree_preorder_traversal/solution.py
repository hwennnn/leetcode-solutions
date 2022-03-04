"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        
        def go(node):
            nonlocal res
            
            if not node: return
            
            res.append(node.val)
            
            for child in node.children:
                go(child)
            
        go(root)
        return res