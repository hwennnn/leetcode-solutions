# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        index = 0
        res = []
        
        def go(node):
            nonlocal index, res
            
            if not node: return True
            
            if node.val != voyage[index]: return False
            
            index += 1
            
            if node.left and node.right and node.left.val != voyage[index] and node.right.val == voyage[index]:
                res.append(node.val)
                
                node.left, node.right = node.right, node.left
            
            return go(node.left) and go(node.right)
        
        return res if go(root) else [-1]
            
            