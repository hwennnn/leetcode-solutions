# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        deq = collections.deque([root])
        res = 0
        
        while deq:
            node = deq.popleft()
            v = node.val
            
            if low <= v <= high:
                res += v
            
            for n in (node.left, node.right):
                if n:
                    deq.append(n)
        
        return res
            
