class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        
        def go(x, path):
            if x == n - 1:
                res.append(path)
                return
            
            for y in graph[x]:
                go(y, path + [y])
            
        go(0, [0])
        
        return res