# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        D = {}
        H = {}
        
        def go(node, depth):
            if not node: return -1
            
            D[node.val] = depth
            height = 1 + max(go(node.left, depth + 1), go(node.right, depth + 1))
            H[node.val] = height
            
            return height
        
        go(root, 0)
        
        levels = defaultdict(list)
        for node, depth in D.items():
            if len(levels[depth]) == 2:
                heappushpop(levels[depth], (H[node], node))
            else:
                heappush(levels[depth], (H[node], node))

        res = []
        for node in queries:
            depth = D[node]
            
            if len(levels[depth]) == 1:
                res.append(depth - 1)
            elif levels[depth][1][1] == node:
                res.append(levels[depth][0][0] + depth)
            else:
                res.append(levels[depth][1][0] + depth)
        
        return res