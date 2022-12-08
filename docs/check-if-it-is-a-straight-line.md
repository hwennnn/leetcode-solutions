---
id: check-if-it-is-a-straight-line
title: Check If It Is a Straight Line
description: Problem Description and Solution for Check If It Is a Straight Line
sidebar_label: 1232. Check If It Is a Straight Line
sidebar_position: 1232
---

# [1232. Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)

```py title=check-if-it-is-a-straight-line.py
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0,y0), (x1,y1) = coordinates[:2]
        
        return all((x1-x0) * (y-y1) == (x-x1) * (y1-y0) for x,y in coordinates)
```


