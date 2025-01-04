---
title: Kruskal's Algorithm
tags:
  - algorithms
  - graph
  - spanning-tree
date: 2024-05-13
---

## Introduction

**Kruskal’s algorithm** is used to find the **minimum/maximum spanning tree**. A minimum spanning tree is a spanning tree whose weight is as small as possible.

## Implementation

```py
def kruskal(N, edges):
    weights = 0
    uf = DSU()

    # edges = (u, v, weight)
    edges.sort(key = lambda x : x[2])

    # To find minimum spanning tree
    for a, b, w in edges:
        if not uf.same(a, b):
            uf.union(a, b)
            weights += w

    return weights
```

## Complexity

- Time complexity: $O(E \log E)$ or $O(E \log V)$

  - Sorting edges: $O(E \log E)$
  - Union-Find operations: $O(E \cdot \alpha(V))$, where $\alpha$ is the inverse Ackermann function
  - Since $\alpha(V)$ grows extremely slowly and is effectively constant, this becomes $O(E)$
  - Overall complexity is dominated by the sorting step

- Space complexity: $O(V + E)$
  - Edge list: $O(E)$
  - Union-Find data structure: $O(V)$
