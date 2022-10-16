# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        def go(node):
            if not node: return (0, 0)
            
            lCount, lValues = go(node.left)
            rCount, rValues = go(node.right)
            
            nodeCount, nodeValues = 1 + lCount + rCount, node.val + lValues + rValues
            
            average = nodeValues // nodeCount
            
            if node.val == average:
                nonlocal res
                
                res += 1
            
            return (nodeCount, nodeValues)
        
        go(root)
        
        return res