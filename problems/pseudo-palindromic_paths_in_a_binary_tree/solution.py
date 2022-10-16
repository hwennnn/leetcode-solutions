# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, mp):
        if not root: return 0
        
        mp[root.val] += 1
        
        count = 0
        if not root.left and not root.right and sum(v&1 for v in mp.values()) <= 1:
            count += 1
        
        count += self.dfs(root.left, mp)
        count += self.dfs(root.right, mp)
        
        mp[root.val] -= 1
        
        return count
        
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.dfs(root, collections.defaultdict(int))