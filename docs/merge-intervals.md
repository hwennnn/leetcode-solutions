---
id: merge-intervals
title: Merge Intervals
description: Problem Description and Solution for Merge Intervals
sidebar_label: 56. Merge Intervals
sidebar_position: 56
---

# [56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

```py title=merge-intervals.py
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        s, e = intervals[0]
        
        for x, y in intervals[1:]:
            if s <= x <= e:
                s = min(s, x)
                e = max(e, y)
            else:
                res.append((s, e))
                s, e = x, y
        
        res.append([s, e])
        
        return res
```


