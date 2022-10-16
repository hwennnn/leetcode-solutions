class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = [0] * n
        
        for x, y in edges:
            in_degree[y] += 1
        
        res = []
        
        for i in range(n):
            if in_degree[i] == 0:
                res.append(i)
        
        return res