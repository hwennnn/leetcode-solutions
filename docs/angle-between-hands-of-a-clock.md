---
id: angle-between-hands-of-a-clock
title: Angle Between Hands of a Clock
description: Problem Description and Solution for Angle Between Hands of a Clock
sidebar_label: 1344. Angle Between Hands of a Clock
sidebar_position: 1344
---

# [1344. Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/)

```py title=angle-between-hands-of-a-clock.py
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h = (hour%12) * 30 + (minutes/60 * 30)
        
        m = minutes/60 * 360
        
        angle = abs(h-m)
        
        if angle > 180:
            angle = 360 - angle
        
        return angle
```


