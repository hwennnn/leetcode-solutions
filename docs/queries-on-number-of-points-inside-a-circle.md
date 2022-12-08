---
id: queries-on-number-of-points-inside-a-circle
title: Queries on Number of Points Inside a Circle
description: Problem Description and Solution for Queries on Number of Points Inside a Circle
sidebar_label: 1828. Queries on Number of Points Inside a Circle
sidebar_position: 1828
---

# [1828. Queries on Number of Points Inside a Circle](https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/)

```py title=queries-on-number-of-points-inside-a-circle.py
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = []
        
        for x, y, r in queries:
            count = 0
            
            for p1,p2 in points:
                dx = abs(p1 - x)
                dy = abs(p2 - y)
                
                count += int(dx**2 + dy**2 <= r**2)
            
            res.append(count)
        
        return res
```


