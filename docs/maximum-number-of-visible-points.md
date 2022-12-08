---
id: maximum-number-of-visible-points
title: Maximum Number of Visible Points
description: Problem Description and Solution for Maximum Number of Visible Points
sidebar_label: 1610. Maximum Number of Visible Points
sidebar_position: 1610
---

# [1610. Maximum Number of Visible Points](https://leetcode.com/problems/maximum-number-of-visible-points/)

```py title=maximum-number-of-visible-points.py
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        
        arr, extra = [], 0
        xx, yy = location
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            arr.append(math.atan2(y - yy, x - xx))
        
        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180

        l = ans = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans + extra
```


