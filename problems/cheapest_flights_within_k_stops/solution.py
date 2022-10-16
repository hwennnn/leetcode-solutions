class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        
        for x, y, weight in flights:
            graph[x].append((weight, y))
        
        pq = [(0, src, k + 1)]
        seen = dict()
        
        while pq:
            d, node, stops = heapq.heappop(pq)
            
            if node == dst: return d
            
            if node in seen and seen[node] >= stops: continue
                
            seen[node] = stops
            
            if stops > 0:
                for weight, nei in graph[node]:
                    heapq.heappush(pq, (d + weight, nei, stops - 1))
        
        return -1