class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0] * n
        graph = [[] for _ in range(n)]
        
        for a,b in paths:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        for i in range(n):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in graph[i]}).pop()
        
        return res