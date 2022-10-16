class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        G = defaultdict(list)
        RG = defaultdict(list)
        
        for x, y, w in edges:
            G[x].append((y, w))
            RG[y].append((x, w))
        
        def dijkstra(graph, src):
            dist = [float('inf')] * n
            dist[src] = 0
            pq = [(0, src)]
            
            while pq:
                d, node = heapq.heappop(pq)
                
                if dist[node] != d: continue
                
                for nei, w in graph[node]:
                    old = dist[nei]
                    new = d + w
                    
                    if new < old:
                        dist[nei] = new
                        heapq.heappush(pq, (new, nei))
            
            return dist
        
        A = dijkstra(G, src1)
        B = dijkstra(G, src2)
        C = dijkstra(RG, dest)
        
        res = float('inf')
        
        for a, b, c in zip(A, B, C):
            res = min(res, a + b + c)
        
        return -1 if res == float('inf') else res
            
            