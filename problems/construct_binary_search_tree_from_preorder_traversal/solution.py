# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        def go(A, bound = float('inf')):
            if not A or A[-1] > bound: return None
            
            node = TreeNode(A.pop())
            node.left = go(A, node.val)
            node.right = go(A, bound)
            
            return node
        
        return go(preorder[::-1])