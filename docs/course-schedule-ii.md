---
id: course-schedule-ii
title: Course Schedule II
description: Problem Description and Solution for Course Schedule II
sidebar_label: 210. Course Schedule II
sidebar_position: 210
---

# [210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)

```py title=course-schedule-ii.py
class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        visited = [0] * n
        res = []
        
        for a, b in prerequisites:
            graph[b].append(a)
        
        def dfs(i):
            if visited[i] == -1:
                return False
            
            if visited[i] == 1:
                return True
            
            visited[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            
            visited[i] = 1
            
            res.append(i)
            return True
        
        for i in range(n):
            if visited[i] == 0 and not dfs(i):
                return []
        
        return res[::-1]
```


