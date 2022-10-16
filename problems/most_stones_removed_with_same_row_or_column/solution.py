class DSU:
    def __init__(self, n):
        self.graph = list(range(n))

    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])

        return self.graph[x]

    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        self.graph[ux] = uy

    def connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        rows = defaultdict(list)
        cols = defaultdict(list)
        
        for i, (x, y) in enumerate(stones):
            rows[x].append(i)
            cols[y].append(i)
        
        dsu = DSU(n)
        
        for row in rows.values():
            for i in range(len(row)):
                for j in range(i + 1, len(row)):
                    dsu.union(row[i], row[j])
        
        for col in cols.values():
            for i in range(len(col)):
                for j in range(i + 1, len(col)):
                    dsu.union(col[i], col[j])
        
        parents = set()
        
        for node in range(n):
            p = dsu.find(node)
            parents.add(p)
        
        return n - len(parents)