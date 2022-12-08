---
id: minimum-time-to-complete-trips
title: Minimum Time to Complete Trips
description: Problem Description and Solution for Minimum Time to Complete Trips
sidebar_label: 2187. Minimum Time to Complete Trips
sidebar_position: 2187
---

# [2187. Minimum Time to Complete Trips](https://leetcode.com/problems/minimum-time-to-complete-trips/)

```py title=minimum-time-to-complete-trips.py
class Solution:
    def minimumTime(self, time: List[int], t: int) -> int:
        n = len(time)
        
        def good(x):
            count = 0
            
            for trip in time:
                count += x // trip
            
            return count >= t
        
        left, right = 1, t * max(time)
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
```


