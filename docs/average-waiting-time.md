---
id: average-waiting-time
title: Average Waiting Time
description: Problem Description and Solution for Average Waiting Time
sidebar_label: 1701. Average Waiting Time
sidebar_position: 1701
---

# [1701. Average Waiting Time](https://leetcode.com/problems/average-waiting-time/)

```py title=average-waiting-time.py
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        res = curr = 0
        
        for a,t in customers:
            curr = max(curr, a) + t
            res += curr - a
        
        return res / n
```


