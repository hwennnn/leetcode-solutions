---
id: distance-between-bus-stops
title: Distance Between Bus Stops
description: Problem Description and Solution for Distance Between Bus Stops
sidebar_label: 1184. Distance Between Bus Stops
sidebar_position: 1184
---

# [1184. Distance Between Bus Stops](https://leetcode.com/problems/distance-between-bus-stops/)

```py title=distance-between-bus-stops.py
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, end: int) -> int:
        a = min(start, end)
        b = max(start, end)
        
        return min(sum(distance[a:b]), sum(distance) - sum(distance[a:b]))
```


