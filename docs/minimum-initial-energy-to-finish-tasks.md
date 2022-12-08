---
id: minimum-initial-energy-to-finish-tasks
title: Minimum Initial Energy to Finish Tasks
description: Problem Description and Solution for Minimum Initial Energy to Finish Tasks
sidebar_label: 1665. Minimum Initial Energy to Finish Tasks
sidebar_position: 1665
---

# [1665. Minimum Initial Energy to Finish Tasks](https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/)

```py title=minimum-initial-energy-to-finish-tasks.py
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x:(x[0] - x[1]))
        
        res = curr = 0
        for cost, mmin in tasks:
            if curr < mmin:
                res += (mmin - curr)
                curr = mmin
            
            curr -= cost
        
        return res
```


