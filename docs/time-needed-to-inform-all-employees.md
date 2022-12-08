---
id: time-needed-to-inform-all-employees
title: Time Needed to Inform All Employees
description: Problem Description and Solution for Time Needed to Inform All Employees
sidebar_label: 1376. Time Needed to Inform All Employees
sidebar_position: 1376
---

# [1376. Time Needed to Inform All Employees](https://leetcode.com/problems/time-needed-to-inform-all-employees/)

```py title=time-needed-to-inform-all-employees.py
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        
        for x, y in enumerate(manager):
            if y == -1: continue
                
            graph[y].append(x)
        
        @cache
        def go(node):
            res = 0
            
            for nei in graph[node]:
                res = max(res, go(nei) + informTime[node])
            
            return res
        
        return go(headID)
```


