---
id: maximum-number-of-robots-within-budget
title: Maximum Number of Robots Within Budget
description: Problem Description and Solution for Maximum Number of Robots Within Budget
sidebar_label: 2398. Maximum Number of Robots Within Budget
sidebar_position: 2398
---

# [2398. Maximum Number of Robots Within Budget](https://leetcode.com/problems/maximum-number-of-robots-within-budget/)

```py title=maximum-number-of-robots-within-budget.py
from sortedcontainers import SortedList

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        largest = SortedList()
        res = i = costs = 0
        
        for j in range(n):
            largest.add(chargeTimes[j])
            costs += runningCosts[j]
            
            total = largest[-1] + (j - i + 1) * costs
            
            while total > budget:
                largest.remove(chargeTimes[i])
                costs -= runningCosts[i]
                i += 1
                total = largest[-1] if largest else 0 + (j - i + 1) * costs
                
            res = max(res, j - i + 1)
        
        return res
```


