class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        graph = collections.defaultdict(dict)
        
        for u, v, w in edges:
            graph[u][v] = graph[v][u] = w
        
        seen = {}
        pq = [(-maxMoves, 0)]
        
        while pq:
            moves, src = heapq.heappop(pq)
            
            if src not in seen:
                seen[src] = -moves
                
                for nei in graph[src]:
                    newMoves = -moves - graph[src][nei] - 1
                    
                    if nei not in seen and newMoves >= 0:
                        heapq.heappush(pq, (-newMoves, nei))
        
        res = len(seen)
        
        for u, v, w in edges:
            res += min(seen.get(u, 0) + seen.get(v, 0), w)
        
        return res