# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root: return 0
        res = 0
        
        def go(node, curr):
            nonlocal res
            
            if not node: return
            
            curr += node.val
            res += mp[curr - targetSum]
            
            mp[curr] += 1
            go(node.left, curr)
            go(node.right, curr)
            mp[curr] -= 1
        
        mp = collections.defaultdict(int)
        mp[0] = 1
        go(root, 0)
    
        return res