class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        m = len(connections)
        
        if m < n - 1: return -1
        
        graph = collections.defaultdict(list)
        visited = [False] * n
        
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
        
        def go(node):
            if visited[node]: return 0
            
            visited[node] = True
            
            for nei in graph[node]:
                go(nei)
            
            return 1
        
        return sum(go(node) for node in range(n)) - 1