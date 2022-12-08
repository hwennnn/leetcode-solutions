---
id: minimum-time-visiting-all-points
title: Minimum Time Visiting All Points
description: Problem Description and Solution for Minimum Time Visiting All Points
sidebar_label: 1266. Minimum Time Visiting All Points
sidebar_position: 1266
---

# [1266. Minimum Time Visiting All Points](https://leetcode.com/problems/minimum-time-visiting-all-points/)

```py title=minimum-time-visiting-all-points.py
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for (prevX,prevY), (currX,currY) in zip(points, points[1:]):
            res += max(abs(prevX-currX), abs(prevY-currY))
        
        return res
```


