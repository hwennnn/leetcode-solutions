---
id: all-ancestors-of-a-node-in-a-directed-acyclic-graph
title: All Ancestors of a Node in a Directed Acyclic Graph
description: Problem Description and Solution for All Ancestors of a Node in a Directed Acyclic Graph
sidebar_label: 2192. All Ancestors of a Node in a Directed Acyclic Graph
sidebar_position: 2192
---

# [2192. All Ancestors of a Node in a Directed Acyclic Graph](https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/)

```py title=all-ancestors-of-a-node-in-a-directed-acyclic-graph.py
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = collections.defaultdict(list)
        visited = [False] * n
        p = collections.defaultdict(set)
        
        for x, y in edges:
            graph[y].append(x)
        
        def go(node):
            if visited[node]:
                return p[node]
            
            visited[node] = True
            parents = set()
            
            for parent in graph[node]:
                parents |= go(parent)
                parents.add(parent)
                    
            p[node] = parents
            return parents
        

        for node in range(n):
            if not visited[node]:
                go(node)
        
        res = []
        
        for i in range(n):
            res.append(sorted(list(p[i])))
        
        return res
```


