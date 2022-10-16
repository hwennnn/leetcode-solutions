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

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)
        emails = collections.defaultdict(list)
        
        for i, account in enumerate(accounts):
            for email in account[1:]:
                emails[email].append(i)
        
        for email, links in emails.items():
            for i in range(len(links) - 1):
                dsu.union(links[i], links[i + 1])
        
        merged = collections.defaultdict(set)
        for email, links in emails.items():
            parent = dsu.find(links[0])
            merged[parent].add(email)
        
        return [[accounts[i][0]] + sorted(list(email)) for i, email in merged.items()]
            
            
        