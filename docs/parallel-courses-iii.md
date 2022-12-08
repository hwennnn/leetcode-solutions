---
id: parallel-courses-iii
title: Parallel Courses III
description: Problem Description and Solution for Parallel Courses III
sidebar_label: 2050. Parallel Courses III
sidebar_position: 2050
---

# [2050. Parallel Courses III](https://leetcode.com/problems/parallel-courses-iii/)

```py title=parallel-courses-iii.py
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = collections.defaultdict(list)
        
        for x, y in relations:
            graph[y - 1].append(x - 1)
        
        @cache
        def go(x):
            res = 0
            
            for node in graph[x]:
                res = max(res, go(node))    
            
            return time[x] + res
        
        return max(go(i) for i in range(n))
```


