# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        cols = defaultdict(list)

        def dfs(node, R, C):
            if not node: return
            
            cols[C].append((C, R, node.val))
            
            dfs(node.left, R + 1, C - 1)
            dfs(node.right, R + 1, C + 1)
        
        dfs(root, 0, 0)
        
        keys = sorted(cols.keys())
        res = []
        
        for key in keys:
            cols[key].sort(key = lambda x : (x[0], x[1], x[2]))
            curr = []
            
            for _, _, val in cols[key]:
                curr.append(val)
                
            res.append(curr)
        
        return res