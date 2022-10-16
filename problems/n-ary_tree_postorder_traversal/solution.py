"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        temp = []
        if root == None: return temp
        def recursion(root,temp):
            for child in root.children:
                recursion(child,temp)
            
            temp.append(root.val)
            
        recursion(root,temp)
        
        return temp
            