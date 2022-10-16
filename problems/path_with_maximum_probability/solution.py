class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [set() for _ in range(n)]
        weights = [0] * n
        weights[start] = 1
        
        for (s, e), weight in zip(edges, succProb):
            graph[s].add((weight, e))
            graph[e].add((weight, s))

        pq = [(-1, start)]
        
        while pq:
            weight, src = heapq.heappop(pq)
            weight = -weight
            
            if weight != weights[src]: continue

            for w, nei in graph[src]:
                old = weights[nei]
                new = weight * w

                if new > old:
                    heapq.heappush(pq, (-new, nei))
                    weights[nei] = new
        
        return weights[end]