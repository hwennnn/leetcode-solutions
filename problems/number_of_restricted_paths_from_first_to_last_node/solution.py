class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        M = 10 ** 9 + 7
        graph = collections.defaultdict(list)
        dist = [float('inf')] * n
        dist[n - 1] = 0
        
        for u, v, w in edges:
            u -= 1
            v -= 1
            
            graph[u].append((w, v))
            graph[v].append((w, u))
        
        pq = [(0, n - 1)]
        
        while pq:
            d, src = heapq.heappop(pq)
            
            if dist[src] != d: continue
            
            for weight, nei in graph[src]:
                old = dist[nei]
                new = dist[src] + weight
                
                if new < old:
                    dist[nei] = new
                    heapq.heappush(pq, (new, nei))
        
        @cache
        def dfs(x):
            if x == n - 1: return 1
            
            res = 0
            for _, nei in graph[x]:
                if dist[x] > dist[nei]:
                    res = (res + dfs(nei)) % M
            
            return res
        
        return dfs(0)