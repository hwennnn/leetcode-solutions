---
id: reachable-nodes-in-subdivided-graph
title: Reachable Nodes In Subdivided Graph
description: Problem Description and Solution for Reachable Nodes In Subdivided Graph
sidebar_label: 882. Reachable Nodes In Subdivided Graph
sidebar_position: 882
---

# [882. Reachable Nodes In Subdivided Graph](https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/)

```py title=reachable-nodes-in-subdivided-graph.py
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
```


