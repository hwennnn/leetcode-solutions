---
title: Dijkstra's Algorithm
tags:
  - algorithms
  - graph
date: 2024-05-10
---

## Introduction

**Dijkstra’s algorithm** finds shortest paths from starting node to all nodes of the graph. It is more efficient and can be used for processing large graphs. However, the algorithm requires that there are no negative weight edges in the graph. Each edge is only processed once.

## Implementation

```py
def dijkstra(N, start, graph):
    distance = [inf] * N
    distance[start] = 0
    pq = [(0, start)] # (weight, node)

    while pq:
        w, node = heappop(pq)
        if w != distance[node]: continue

        for adj, w2 in graph[node]:
            newDist = w + w2
            if newDist < distance[adj]:
                distance[adj] = newDist
                heappush(pq, (newDist, adj))
```

> [!note]
> It is important to check `if w != distance[node]` to avoid processing the same node multiple times.

## Complexity

- Time complexity: $O(V \log V + E)$, where $V$ is the number of vertices and $E$ is the number of edges
  - Each vertex is added/removed from the priority queue once: $O(V \log V)$
  - Each edge is processed once: $O(E)$
- Space complexity: $O(V + E)$
  - Priority queue can contain at most $V$ vertices: $O(V)$
  - Graph representation (adjacency list): $O(E)$
