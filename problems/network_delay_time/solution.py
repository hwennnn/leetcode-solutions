class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        k -= 1
        
        graph = collections.defaultdict(list)
        weights = [float('inf')] * n
        weights[k] = 0
        
        for u, v, w in times:
            u -= 1
            v -= 1
            graph[u].append((v, w))

        pq = [(0, k)]
        
        while pq:
            weight, node = heapq.heappop(pq)
            
            if weight != weights[node]: continue

            for nei, w in graph[node]:
                old = weights[nei]
                new = weight + w

                if new < old:
                    heapq.heappush(pq, (new, nei))
                    weights[nei] = new
        
        res = max(weights)
        return -1 if res == float('inf') else res