class UnionFind:
    def __init__(self):
        self._parent = {}
        self._size = {}

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self._size[a] < self._size[b]:
            a, b = b, a
        self._parent[b] = a
        self._size[a] += self._size[b]

    def find(self, x):
        if x not in self._parent:
            self._parent[x] = x
            self._size[x] = 1
        while self._parent[x] != x:
            self._parent[x] = self._parent[self._parent[x]]
            x = self._parent[x]
        return x
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = []
        n = len(points)
        
        for i in range(n):
            a, b = points[i]
            for j in range(i + 1, n):
                c, d = points[j]
                
                dist = abs(a - c) + abs(b - d)
                graph.append((dist, i, j))
        
        res = 0 
        uf = UnionFind()
        
        for dist, i, j in sorted(graph):
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                res += dist
        
        return res