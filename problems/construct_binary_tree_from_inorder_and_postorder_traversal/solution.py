# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(inorder)
        mp = {}
        
        for i, x in enumerate(inorder):
            mp[x] = i
        
        def go(low, high):
            if low > high: return None
            
            x = postorder.pop()
            node = TreeNode(x)
            mid = mp[x]
            node.right = go(mid + 1, high)
            node.left = go(low, mid - 1)
            
            return node
        
        return go(0, n - 1)
            