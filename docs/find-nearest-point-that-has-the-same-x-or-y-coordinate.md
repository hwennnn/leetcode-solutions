---
id: find-nearest-point-that-has-the-same-x-or-y-coordinate
title: Find Nearest Point That Has the Same X or Y Coordinate
description: Problem Description and Solution for Find Nearest Point That Has the Same X or Y Coordinate
sidebar_label: 1779. Find Nearest Point That Has the Same X or Y Coordinate
sidebar_position: 1779
---

# [1779. Find Nearest Point That Has the Same X or Y Coordinate](https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/)

```py title=find-nearest-point-that-has-the-same-x-or-y-coordinate.py
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        distance = float('inf')
        
        for index, (x2, y2) in enumerate(points):
            if x2 == x or y2 == y:
                d = abs(x2 - x) + abs(y2 - y)
                if d < distance:
                    distance = d
                    res = index
        
        return res if distance != float('inf') else -1
```


