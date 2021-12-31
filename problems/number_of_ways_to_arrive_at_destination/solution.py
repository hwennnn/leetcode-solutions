class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in roads:
            graph[u].append((w, v))
            graph[v].append((w, u))
            
        M = 10 ** 9 + 7
        dest = [float('inf')] * n
        dest[0] = 0
        count = [0] * n
        count[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            d, src = heapq.heappop(pq)
            
            if src == n - 1:
                return count[src] % M
            
            if dest[src] != d: continue
            
            for weight, nei in graph[src]:
                old = dest[nei]
                new = dest[src] + weight
                
                if new == old:
                    count[nei] += count[src]
                elif new < old:
                    dest[nei] = new
                    heapq.heappush(pq, (new, nei))
                    count[nei] = count[src]