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
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        N = len(vals)
        res = 0
        uf = UnionFind()
        G = defaultdict(list)
        V = defaultdict(list)
        
        for a, b in edges:
            G[a].append(b)
            G[b].append(a)
        
        for node, val in enumerate(vals):
            V[val].append(node)
        
        for value in sorted(V.keys()):
            for node in V[value]:
                for adj in G[node]:
                    if vals[adj] <= value:
                        uf.union(node, adj)
            
            cnt = defaultdict(int)
            for node in V[value]:
                parent = uf.find(node)
                cnt[parent] += 1
                res += cnt[parent]
        
        return res