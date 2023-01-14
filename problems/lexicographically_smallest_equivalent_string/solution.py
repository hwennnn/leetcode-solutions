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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()

        for a, b in zip(s1, s2):
            uf.union(a, b)
        
        parents = defaultdict(list)

        for x in s1 + s2:
            parent = uf.find(x)
            parents[parent].append(x)
        
        for key in parents.keys():
            parents[key].sort()

        res = []

        for x in baseStr:
            parent = uf.find(x)
            if parent not in parents:
                res.append(x)
            else:
                res.append(parents[parent][0])

        return "".join(res)