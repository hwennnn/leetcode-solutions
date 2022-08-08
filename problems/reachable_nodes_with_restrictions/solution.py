class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        visited = [False] * n
        
        for node in restricted:
            visited[node] = True
        
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        res = 0
        
        def dfs(node):
            nonlocal res
            
            visited[node] = True
            
            res = 1
            
            for nei in graph[node]:
                if not visited[nei]:
                    res += dfs(nei)
            
            return res
            
        return dfs(0)