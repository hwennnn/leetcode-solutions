class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = [[] for _ in range(n)]
        visited = [False] * n
        res = 0
        
        for node, relations in enumerate(isConnected):
            for nei, has in enumerate(relations):
                if node == nei: continue
                if has:
                    graph[node].append(nei)
        
        def go(node):
            visited[node] = True
            
            for nei in graph[node]:
                if not visited[nei]:
                    go(nei)
        
        for i in range(n):
            if not visited[i]:
                res += 1
                go(i)
        
        return res