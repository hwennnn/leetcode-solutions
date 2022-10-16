class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = [False] * n
        graph = defaultdict(list)
        
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(-x)
        
        def go(node):
            visited[node] = True
            res = 0
            
            for nei in graph[node]:
                if not visited[abs(nei)]:
                    visited[abs(nei)] = True
                    res += go(abs(nei)) + int(nei > 0)
            
            return res
        
        return go(0)