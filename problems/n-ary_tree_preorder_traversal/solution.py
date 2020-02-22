"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        temp = []
        if root == None: return None
        
        def recursion(root,temp):
            temp.append(root.val)
            for child in root.children:
                recursion(child,temp)
                
        
        recursion(root,temp)
        
        return temp