---
id: remove-covered-intervals
title: Remove Covered Intervals
description: Problem Description and Solution for Remove Covered Intervals
sidebar_label: 1288. Remove Covered Intervals
sidebar_position: 1288
---

# [1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)

```py title=remove-covered-intervals.py
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        res = right = 0
        
        intervals.sort(key = lambda x:(x[0],-x[1]))
        
        for start,end in intervals:
            res += end > right
            right = max(right, end)
        
        return res
```


