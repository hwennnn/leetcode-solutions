---
id: capacity-to-ship-packages-within-d-days
title: Capacity To Ship Packages Within D Days
description: Problem Description and Solution for Capacity To Ship Packages Within D Days
sidebar_label: 1011. Capacity To Ship Packages Within D Days
sidebar_position: 1011
---

# [1011. Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

```py title=capacity-to-ship-packages-within-d-days.py
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        
        def good(target):
            mmax = s = 0
            day = 1
            
            for x in weights:
                if s + x > target:
                    s = x
                    day += 1
                else:
                    s += x
                mmax = max(mmax, s)
            
            return day <= days and mmax <= target
        
        left, right = 1, total
        
        while left < right:
            mid = left + (right - left) // 2
            
            if good(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
```


