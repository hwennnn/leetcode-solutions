---
id: minimum-number-of-arrows-to-burst-balloons
title: Minimum Number of Arrows to Burst Balloons
description: Problem Description and Solution for Minimum Number of Arrows to Burst Balloons
sidebar_label: 452. Minimum Number of Arrows to Burst Balloons
sidebar_position: 452
---

# [452. Minimum Number of Arrows to Burst Balloons](https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/)

```py title=minimum-number-of-arrows-to-burst-balloons.py
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key = lambda x : x[1])
        shoot = points[0][1]
        res = 1
        
        for i in range(1, n):
            
            if points[i][0] > shoot:
                res += 1
                shoot = points[i][1]
        
        return res
        
```


