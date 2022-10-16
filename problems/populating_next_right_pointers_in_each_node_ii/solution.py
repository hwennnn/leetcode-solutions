"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        level = []
        if root:
            level.append(root)
        
        while len(level) > 0:
            next_level = []
            
            for prev, node in zip(level, level[1:]):
                prev.next = node
            
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            
            level = next_level
        
        return root
                