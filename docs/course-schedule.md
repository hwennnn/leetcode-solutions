---
id: course-schedule
title: Course Schedule
description: Problem Description and Solution for Course Schedule
sidebar_label: 207. Course Schedule
sidebar_position: 207
---

# [207. Course Schedule](https://leetcode.com/problems/course-schedule/)

```py title=course-schedule.py
class Solution:
    def canFinish(self, n: int, A: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        visited = [0] * n
        
        for a, b in A:
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
            
            return True
        
        for i in range(n):
            if not dfs(i): 
                return False
        
        return True
```


