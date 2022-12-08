---
id: divide-intervals-into-minimum-number-of-groups
title: Divide Intervals Into Minimum Number of Groups
description: Problem Description and Solution for Divide Intervals Into Minimum Number of Groups
sidebar_label: 2406. Divide Intervals Into Minimum Number of Groups
sidebar_position: 2406
---

# [2406. Divide Intervals Into Minimum Number of Groups](https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/)

```py title=divide-intervals-into-minimum-number-of-groups.py
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        A = []
        
        for s, e in intervals:
            A.append((s, 1))
            A.append((e + 1, -1))
        
        A.sort()
        res = curr = 0
        
        for x, d in A:
            curr += d
            res = max(res, curr)
        
        return res
```


