class Solution:
    def findCircleNum(self, graphs: List[List[int]]) -> int:
        n = len(graphs)
        seen = set()
        
        def dfs(i):
            for nei, adj in enumerate(graphs[i]):
                if adj and nei not in seen:
                    seen.add(nei)
                    dfs(nei)
        
        res = 0
        for i in range(n):
            if i not in seen:
                res += 1
                dfs(i)
        
        return res