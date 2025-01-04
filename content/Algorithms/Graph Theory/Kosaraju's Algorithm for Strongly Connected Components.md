---
title: Kosaraju's Algorithm for Strongly Connected Components
tags:
  - algorithms
  - graph
  - strongly-connected-components
  - topological-sort
date: 2023-10-22
---

## Introduction

### What is Strongly Connected Components (SCC)?

![[kosaraju-scc.png]]
A **SCC** in a [[Introduction to Graph Theory#^directed-graph|Directed Graph]] is a subset of vertices where every vertex is reachable from every other vertex within the same subset. In simpler terms, it's a group of vertices in a directed graph where you can travel from any vertex to any other vertex within the same group, following the direction of edges.

## Implementation

```py
N = len(edges)

# 1. DFS on the graph to generate toposort
visited = [False] * N
topo = []

def dfs(node):
    if visited[node]: return

    visited[node] = True

    dfs(edges[node])

    topo.append(node)

for node in range(N):
    dfs(node)

# 2. reverse the graph
transpose = defaultdict(list)

for node, adj in enumerate(edges):
    transpose[adj].append(node)

# 3. DFS on the reversed graph to find the cycles
visited = [False] * N
comp = 0
scc = [-1] * N
sccList = [[] for _ in range(N)]

def dfs2(node):
    if visited[node]: return

    visited[node] = True
    scc[node] = comp
    sccList[comp].append(node)

    for adj in transpose[node]:
        dfs2(adj)

while topo:
    node = topo.pop()

    if not visited[node]:
        dfs2(node)
        comp += 1

```

## Complexity

- Time complexity: $O(V+E)$
- Space complexity: $O(V+E)$

## Resources

1. [Strongly Connected Components - Programiz](https://www.programiz.com/dsa/strongly-connected-components)
