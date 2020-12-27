# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        deq = collections.deque([root])
        res = 0
        
        while deq:
            l = len(deq)
            res = 0
            
            while l:
                node = deq.popleft()
                res += node.val
                
                for n in (node.left, node.right):
                    if n: deq.append(n)
                l -= 1
            

        return res