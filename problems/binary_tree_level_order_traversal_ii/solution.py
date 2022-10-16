# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        q, res = collections.deque([(root, 0)]), []
        
        while q:
            node, lvl = q.popleft()
            
            if node:
                if len(res) < lvl + 1:
                    res.insert(0, [])
                res[-(lvl+1)].append(node.val)
                for i in (node.left,node.right):
                    if i:
                        q.append([i, lvl+1])
                
        return res