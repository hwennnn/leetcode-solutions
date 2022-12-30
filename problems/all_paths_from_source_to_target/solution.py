class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        N = len(graph)
        res = []

        def dfs(node, path):
            nonlocal res

            if node == N - 1:
                res.append(path)
                return
            
            for nei in graph[node]:
                dfs(nei, path + [nei])
        
        dfs(0, [0])

        return res