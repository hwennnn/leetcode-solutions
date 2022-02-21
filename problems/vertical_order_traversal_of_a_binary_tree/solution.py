# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp = collections.defaultdict(list)
        
        queue = deque([(root, 0, 0)])
        
        while queue:
            node, row, col = queue.popleft()
            
            mp[col].append((row, node.val))
            
            if node.left:
                queue.append((node.left, row + 1, col - 1))
            
            if node.right:
                queue.append((node.right, row + 1, col + 1))
        
        n = len(mp)
        res = []
        keys = sorted(mp.keys())
        
        for key in keys:
            res.append(col for _, col in sorted(mp[key], key = lambda x : (x[0], x[1])))
        
        return res