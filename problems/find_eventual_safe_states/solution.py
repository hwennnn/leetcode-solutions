class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        res = []
        color = [0] * n
        
        def go(node):
            if len(graph[node]) == 0: return True
            
            if color[node] != 0: return color[node] == 1
            
            for nei in graph[node]:
                color[node] = 2
                if not go(nei): 
                    return False
                color[node] = 1
            
            return True
        
        return [node for node in range(n) if go(node)]
        
        