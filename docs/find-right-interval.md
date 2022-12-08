---
id: find-right-interval
title: Find Right Interval
description: Problem Description and Solution for Find Right Interval
sidebar_label: 436. Find Right Interval
sidebar_position: 436
---

# [436. Find Right Interval](https://leetcode.com/problems/find-right-interval/)

```py title=find-right-interval.py
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        A = sorted([(x, i) for i, (x, _) in enumerate(intervals)])

        res = []

        for start, end in intervals:
            index = bisect.bisect_left(A, (end, ))
            
            if index < n:
                res.append(A[index][1])
            else:
                res.append(-1)
        
        return res
        
```


