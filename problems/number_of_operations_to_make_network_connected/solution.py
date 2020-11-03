class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return - 1
        
        s = [set() for _ in range(n)]
        
        for c1,c2 in connections:
            s[c1].add(c2)
            s[c2].add(c1)
        
        seen = [0] * n
        
        def dfs(i):
            if seen[i]: return 0
            seen[i] = 1
            
            for j in s[i]: dfs(j)
            
            return 1
        
        return sum(dfs(i) for i in range(n)) - 1