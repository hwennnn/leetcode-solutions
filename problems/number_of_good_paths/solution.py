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
        graph = defaultdict(list)
        uf = UnionFind()
        V = defaultdict(list)
        res = 0

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for node, val in enumerate(vals):
            V[val].append(node)
        
        for val in sorted(V.keys()):
            for node in V[val]:
                for adj in graph[node]:
                    if vals[adj] <= val:
                        uf.union(node, adj)
            
            cnt = defaultdict(int)
            for node in V[val]:
                parent = uf.find(node)
                cnt[parent] += 1
                res += cnt[parent]
        
        return res
            

