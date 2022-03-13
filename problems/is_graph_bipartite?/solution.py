class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        coloured = {}
        
        def go(node):
            for nei in graph[node]:
                if nei in coloured:
                    if coloured[nei] != -coloured[node]:
                        return False
                else:
                    coloured[nei] = -coloured[node]
                    if not go(nei):
                        return False
            
            return True
                
        
        for node in range(n):
            if node not in coloured:
                coloured[node] = 1
                if not go(node):
                    return False
        
        return True