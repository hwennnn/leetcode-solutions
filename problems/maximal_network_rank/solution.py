class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        cities = [0] * n
        s = [[False] * n for _ in range(n)]
        
        for a,b in roads:
            cities[a] += 1
            cities[b] += 1
            s[a][b] = True
            s[b][a] = True
        
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                c = cities[i] + cities[j]
                c -= s[i][j]
                res = max(res, c)
            
        return res
