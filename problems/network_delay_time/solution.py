class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        weights = [float('inf')] * n
        weights[k - 1] = 0
        graph = defaultdict(list)
        
        for u, v, w in times:
            u -= 1
            v -= 1
            graph[u].append((v, w))
        
        pq = [(0, k - 1)]
        
        while pq:
            weight, node = heappop(pq)
            
            if weights[node] != weight: continue
            
            for nei, w in graph[node]:
                old = weights[nei]
                new = weight + w
                
                if new < old:
                    weights[nei] = new
                    heappush(pq, (new, nei))
        
        ans = max(weights)
        
        return -1 if ans == float('inf') else ans