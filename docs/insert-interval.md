---
id: insert-interval
title: Insert Interval
description: Problem Description and Solution for Insert Interval
sidebar_label: 57. Insert Interval
sidebar_position: 57
---

# [57. Insert Interval](https://leetcode.com/problems/insert-interval/)

```py title=insert-interval.py
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        sx, sy = newInterval
        left, right = [], []
        
        for x, y in intervals:
            if y < sx:
                left.append([x, y])
            elif x > sy:
                right.append([x, y])
            else:
                sx = min(sx, x)
                sy = max(sy, y)
                
        return left + [[sx, sy]] + right
```


