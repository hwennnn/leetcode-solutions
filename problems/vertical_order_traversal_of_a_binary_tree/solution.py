# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        mp = collections.defaultdict(list)
        
        deq = collections.deque([(root, (0,0))])
        
        while deq:
            l = len(deq)
            
            while l > 0:
                node, (x, y) = deq.popleft()
                mp[x].append((y, node.val))
                
                if node.left:
                    deq.append((node.left, (x-1, y-1)))
                
                if node.right:
                    deq.append((node.right, (x+1, y-1)))
                    
                l -= 1
        
        res = []
        for k in sorted(mp):
            values = [v[1] for v in sorted(mp[k], key = lambda x:(-x[0], x[1]))]
            res.append(values)
        
        return res