class UnionFind:
    def __init__(self):
        self._parent = {}
        self.segmentSum = {}
        self.maxSegmentSum = 0
    
    def merge(self, u, value):
        self._parent[u] = u
        self.segmentSum[u] = value
        self.maxSegmentSum = max(self.maxSegmentSum, value)
        
        if u - 1 in self._parent:
            self.union(u, u - 1)
        
        if u + 1 in self._parent:
            self.union(u, u + 1)
    
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return

        self.segmentSum[a] += self.segmentSum[b]
        self._parent[b] = a
        self.maxSegmentSum = max(self.maxSegmentSum, self.segmentSum[a])

    def find(self, x):
        if x != self._parent[x]:
            self._parent[x] = self.find(self._parent[x])

        return self._parent[x]

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        uf = UnionFind()
        res = [0] * n
        
        for i in range(n - 1, -1, -1):
            res[i] = uf.maxSegmentSum
            u = removeQueries[i]
            uf.merge(u, nums[u])
        
        return res
        