---
id: minimum-speed-to-arrive-on-time
title: Minimum Speed to Arrive on Time
description: Problem Description and Solution for Minimum Speed to Arrive on Time
sidebar_label: 1870. Minimum Speed to Arrive on Time
sidebar_position: 1870
---

# [1870. Minimum Speed to Arrive on Time](https://leetcode.com/problems/minimum-speed-to-arrive-on-time/)

```py title=minimum-speed-to-arrive-on-time.py
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        n = len(dist)

        def good(x):
            t = 0
            
            for i, d in enumerate(dist):
                if i != n - 1:
                    h = math.ceil(d / x)
                else:
                    h = d / x

                t += h

            return t <= hour
            

        left, right = 1, 10 ** 7 + 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left if left <= 10 ** 7 else -1
            
        
```


