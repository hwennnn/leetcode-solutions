# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        res = 0
        
        def go(node, s):
            nonlocal res
            
            if not node: return
            
            s += node.val
            res += mp[s - targetSum]
            
            mp[s] += 1
            go(node.left, s)
            go(node.right, s)
            mp[s] -= 1
            
        go(root, 0)
        
        return res