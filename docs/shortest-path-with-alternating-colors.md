---
id: shortest-path-with-alternating-colors
title: Shortest Path with Alternating Colors
description: Problem Description and Solution for Shortest Path with Alternating Colors
sidebar_label: 1129. Shortest Path with Alternating Colors
sidebar_position: 1129
---

# [1129. Shortest Path with Alternating Colors](https://leetcode.com/problems/shortest-path-with-alternating-colors/)

```py title=shortest-path-with-alternating-colors.py
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = defaultdict(list), defaultdict(list)
        queue = collections.deque()
        visited = set()
        res = [-1] * n
        res[0] = 0
        
        for x, y in redEdges:
            red[x].append(y)
            if x == 0:
                queue.append((y, 1, True))
        
        for x, y in blueEdges:
            blue[x].append(y)
            if x == 0:
                queue.append((y, 1, False))
        
        while queue:
            node, distance, isRed = queue.popleft()
            
            if res[node] == -1 or distance < res[node]:
                res[node] = distance
            
            if isRed:
                for nei in blue[node]:
                    p = (nei, True)
                    if p not in visited:
                        visited.add(p)
                        queue.append((nei, distance + 1, False))
            else:
                for nei in red[node]:
                    p = (nei, False)
                    if p not in visited:
                        visited.add(p)
                        queue.append((nei, distance + 1, True))
        
        return res
        
        
```


