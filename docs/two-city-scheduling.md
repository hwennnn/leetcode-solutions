---
id: two-city-scheduling
title: Two City Scheduling
description: Problem Description and Solution for Two City Scheduling
sidebar_label: 1029. Two City Scheduling
sidebar_position: 1029
---

# [1029. Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)

```py title=two-city-scheduling.py
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        firstCity = [a for a, b in costs]
        diff = sorted([b - a for a, b in costs])
        
        return sum(firstCity) + sum(diff[:n])
```


