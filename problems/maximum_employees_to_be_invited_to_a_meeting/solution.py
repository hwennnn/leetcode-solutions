class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        graph = collections.defaultdict(list)
        
        for u, v in enumerate(favorite):
            graph[v].append(u)
        
        m = [-1] * n
        
        def dfs(u):
            if m[u] != -1: return m[u]
            
            res = 0
            
            for nei in graph[u]:
                res = max(res, dfs(nei))
            
            m[u] = 1 + res
            
            return m[u]
        
        res1 = 0
        for u, v in enumerate(favorite):
            if m[u] != -1 or u != favorite[v]: continue
            
            m[u] = m[v] = 0
            
            a = 0
            for nei in graph[u]:
                if nei == v: continue
                a = max(a, dfs(nei))
            
            b = 0
            for nei in graph[v]:
                if nei == u: continue
                b = max(b, dfs(nei))
            
            res1 += a + b + 2
        
        res2 = 0
        
        def dfs2(u):
            t = 0
            seen = {}
            
            while u not in seen:
                if m[u] != -1: return 0
                seen[u] = t
                u = favorite[u]
                t += 1
            
            for v in seen.keys():
                m[v] = 0
            
            return t - seen[u]
        
        for u in range(n):
            if m[u] != -1: continue
            
            res2 = max(res2, dfs2(u))
        
        return max(res1, res2)
            
                