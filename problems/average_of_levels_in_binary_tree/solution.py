# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        deq = collections.deque([root])
        
        while deq:
            n = len(deq)
            total = 0
            
            for _ in range(n):
                node = deq.popleft()
                total += node.val
                
                for leaf in (node.left, node.right):
                    if leaf:
                        deq.append(leaf)
                
            res.append(total/n)

        return res
        
        