# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        mp = defaultdict(int)
        mp[root] = 1
        res = 1
        
        while queue:
            n = len(queue)
            start = end = -1
            
            for index in range(n):
                node = queue.popleft()
                
                if index == 0:
                    start = mp[node]
                elif index == n - 1:
                    end = mp[node]
                
                if node.left:
                    queue.append(node.left)
                    mp[node.left] = 2 * mp[node]
                    
                if node.right:
                    queue.append(node.right)
                    mp[node.right] = 2 * mp[node] + 1
            
            res = max(res, end - start + 1)
                    
        return res