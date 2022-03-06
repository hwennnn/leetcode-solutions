class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        
        def go(node, path):
            if node == n - 1:
                res.append(path)
                return
            
            for nei in graph[node]:
                go(nei, path + [nei])
        
        go(0, [0])
        
        return res