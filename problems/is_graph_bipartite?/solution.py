class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(i):
            for nei in graph[i]:
                if nei in coloured:
                    if coloured[nei] == coloured[i]:
                        return False
                else:
                    coloured[nei] = -coloured[i]
                    if not dfs(nei):
                        return False
            
            return True
                    
                   
        coloured = {}
        
        for i in range(len(graph)):
            if i not in coloured:
                coloured[i] = 1
                if not dfs(i):
                    return False
        
        return True
            