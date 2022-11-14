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
    def removeStones(self, stones: List[List[int]]) -> int:
        N = len(stones)
        uf = UnionFind()
        R = defaultdict(list)
        C = defaultdict(list)

        for index, (x, y) in enumerate(stones):
            R[x].append(index)
            C[y].append(index)
        
        for values in R.values():
            for i in range(1, len(values)):
                uf.union(values[i], values[i - 1])
        
        for values in C.values():
            for i in range(1, len(values)):
                uf.union(values[i], values[i - 1])
        
        parents = set()
        for i in range(N):
            parent = uf.find(i)
            parents.add(parent)
        
        return N - len(parents)



