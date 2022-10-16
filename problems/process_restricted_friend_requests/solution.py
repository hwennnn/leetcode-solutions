class DSU:
    def __init__(self, n):
        self.p = list(range(n))
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        
        return self.p[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        self.p[px] = py
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        res = []
        dsu = DSU(n)
        
        for x, y in requests:
            px, py = dsu.find(x), dsu.find(y)
            valid = True
            
            if not dsu.connected(x, y):
                for a, b in restrictions:
                    pa, pb = dsu.find(a), dsu.find(b)
                    
                    if (pa == px and pb == py) or (pa == py and pb == px):
                        valid = False
                        break
                        
            res.append(valid)
            if valid:
                dsu.union(x, y)
        
        return res