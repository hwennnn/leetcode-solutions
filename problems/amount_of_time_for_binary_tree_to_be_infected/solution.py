# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        time = 0
        graph = defaultdict(list)
        N = 0
        
        def dfs(node):
            nonlocal N
            
            if not node: return
            
            N += 1    
            
            if node.left:
                graph[node.left.val].append(node.val)
                graph[node.val].append(node.left.val)
            
            if node.right:
                graph[node.right.val].append(node.val)
                graph[node.val].append(node.right.val)
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        
        if N == 1: return 0
        
        s = [start]
        visited = defaultdict(lambda : False)
        visited[start] = True
        
        while s:
            nxt = []
            
            for node in s:
                for nei in graph[node]:
                    if not visited[nei]:
                        visited[nei] = True
                        nxt.append(nei)
            
            time += 1
            s = nxt
        
        return time - 1