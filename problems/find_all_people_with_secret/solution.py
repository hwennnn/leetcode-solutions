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
    
    def disconnect(self, x):
        self.graph[x] = x

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        m = len(meetings)
        dsu = DSU(n)
        dsu.union(0, firstPerson)
        meetings.sort(key = lambda x : x[2])
        people = set()
        
        i = 0
        while i < m:
            people.clear()
            
            time = meetings[i][2]
            
            while i < m and meetings[i][2] == time:
                x, y, _ = meetings[i]
                dsu.union(x, y)
                people.add(x)
                people.add(y)
                i += 1
            
            for p in people:
                if not dsu.connected(0, p):
                    dsu.disconnect(p)
                    
        res = []
        for i in range(n):
            if dsu.connected(0, i):
                res.append(i)
        
        return res
            
            