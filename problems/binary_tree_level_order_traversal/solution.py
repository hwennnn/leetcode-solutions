# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        
        res = []
        deq = collections.deque([root])
        
        while len(deq) > 0:
            tmp = []
            l = len(deq)
            
            while l > 0:
                node = deq.popleft()
                tmp.append(node.val)
                
                for n in (node.left, node.right):
                    if n:
                        deq.append(n)
                
                l -= 1
            
            res.append(tmp)
        
        return res