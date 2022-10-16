# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = res = 1
        mmax = float('-inf')
        q = collections.deque([root])
        
        while q:
            val = 0
            n = len(q)
            
            for _ in range(n):
                node = q.popleft()
                val += node.val
                for leaf in (node.left, node.right):
                    if leaf:
                        q.append(leaf)
            
            if val > mmax:
                res = level
                mmax = val

            level += 1
        
        return res