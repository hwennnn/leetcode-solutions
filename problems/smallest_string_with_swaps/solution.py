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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind()
        res = [""] * n
        
        for a, b in pairs:
            uf.union(a, b)
        
        groups = defaultdict(list)
        indexes = defaultdict(list)
        
        for i in range(n):
            parent = uf.find(i)
            groups[parent].append(s[i])
            indexes[parent].append(i)
        
        for g in groups.keys():
            groups[g].sort()
            indexes[g].sort()
            
            for i, index in enumerate(indexes[g]):
                res[index] = groups[g][i]
        
        return "".join(res)
        
        