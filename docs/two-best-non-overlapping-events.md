---
id: two-best-non-overlapping-events
title: Two Best Non-Overlapping Events
description: Problem Description and Solution for Two Best Non-Overlapping Events
sidebar_label: 2054. Two Best Non-Overlapping Events
sidebar_position: 2054
---

# [2054. Two Best Non-Overlapping Events](https://leetcode.com/problems/two-best-non-overlapping-events/)

```py title=two-best-non-overlapping-events.py
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        A = []
        
        for start, end, value in events:
            A.append((start, 1, value))
            A.append((end + 1, -1, value))
        
        A.sort()
        currMax = res = 0
        
        for curr, t, x in A:
            if t == 1:
                res = max(res, currMax + x)
            else:
                currMax = max(currMax, x)
        
        return res
```


