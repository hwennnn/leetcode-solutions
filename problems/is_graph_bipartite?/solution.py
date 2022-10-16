class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = defaultdict(int)
        
        def go(x):
            for node in graph[x]:
                if node not in color:
                    color[node] = -color[x]
                    if not go(node):
                        return False
                else:
                    if color[x] == color[node]:
                        return False
            
            return True
        
        for i in range(n):
            if i not in color:
                color[i] = 1
                if not go(i):
                    return False
        
        return True
                
                