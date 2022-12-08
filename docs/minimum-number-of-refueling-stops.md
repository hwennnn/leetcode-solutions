---
id: minimum-number-of-refueling-stops
title: Minimum Number of Refueling Stops
description: Problem Description and Solution for Minimum Number of Refueling Stops
sidebar_label: 871. Minimum Number of Refueling Stops
sidebar_position: 871
---

# [871. Minimum Number of Refueling Stops](https://leetcode.com/problems/minimum-number-of-refueling-stops/)

```py title=minimum-number-of-refueling-stops.py
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        available = [-startFuel]
        res, curr = -1, 0
        i = 0
        
        while available and curr < target:
            fuel = -(heapq.heappop(available))
            res += 1
            curr += fuel
            
            while i < len(stations) and curr >= stations[i][0]:
                heapq.heappush(available, -stations[i][1])
                i += 1
            
        return res if curr >= target else -1
```


