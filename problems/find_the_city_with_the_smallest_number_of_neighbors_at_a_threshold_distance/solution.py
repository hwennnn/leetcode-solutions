class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = collections.defaultdict(list)
        
        for x, y, weight in edges:
            graph[x].append((weight, y))
            graph[y].append((weight, x))
        
        def dijkstra(src):
            weights = [float('inf')] * n
            weights[src] = 0
            
            pq = [(0, src)]
            
            while pq:
                weight, node = heapq.heappop(pq)
                
                if weight != weights[node]: continue
                
                for w, nei in graph[node]:
                    old = weights[nei]
                    new = weights[node] + w
                    
                    if new < old:
                        heapq.heappush(pq, (new, nei))
                        weights[nei] = new
            
            count = 0
            
            for weight in weights:
                if weight <= distanceThreshold:
                    count += 1
            
            return count - 1
        
        res = -1
        smallest = float('inf')
        
        for i in range(n):
            d = dijkstra(i)
            
            if d <= smallest:
                res = i
                smallest = d
        
        return res