class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def dfs(curr, path):
            if curr == len(graph) - 1: res.append(path)
            else:
                for nei in graph[curr]:
                    dfs(nei, path + [nei])
        
        res = []
        dfs(0, [0])
        
        return res