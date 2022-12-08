---
id: count-unreachable-pairs-of-nodes-in-an-undirected-graph
title: Count Unreachable Pairs of Nodes in an Undirected Graph
description: Problem Description and Solution for Count Unreachable Pairs of Nodes in an Undirected Graph
sidebar_label: 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
sidebar_position: 2316
---

# [2316. Count Unreachable Pairs of Nodes in an Undirected Graph](https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/)

```py title=count-unreachable-pairs-of-nodes-in-an-undirected-graph.py
class DSU:
    def __init__(self, n):
        self.graph = list(range(n))

    def find(self, x):
        if self.graph[x] != x:
            self.graph[x] = self.find(self.graph[x])

        return self.graph[x]

    def union(self, x, y):
        ux, uy = self.find(x), self.find(y)
        self.graph[ux] = uy

    def connected(self, x, y):
        return self.find(x) == self.find(y)

    def disconnect(self, x):
        self.graph[x] = x

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        
        for a, b in edges:
            dsu.union(a, b)
        
        parents = [0] * n
        pp = [-1] * n
        
        for node in range(n):
            p = dsu.find(node)
            pp[node] = p
            parents[p] += 1
        
        res = 0
        
        for node in range(n):
            res += n - parents[pp[node]]
        
        return res // 2
```


