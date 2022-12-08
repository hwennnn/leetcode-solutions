---
id: non-overlapping-intervals
title: Non-overlapping Intervals
description: Problem Description and Solution for Non-overlapping Intervals
sidebar_label: 435. Non-overlapping Intervals
sidebar_position: 435
---

# [435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

```py title=non-overlapping-intervals.py
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        
        if n < 2: return 0
        
        intervals.sort(key = lambda x : x[0])
        
        last = intervals[0][1]
        count = 0
        
        for pairs in intervals[1:]:
            if pairs[0] < last:
                count += 1
                last = min(pairs[1], last)
                
            else:
                last = pairs[1]
            
            
        
        return count
```


