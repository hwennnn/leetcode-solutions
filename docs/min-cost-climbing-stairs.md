---
id: min-cost-climbing-stairs
title: Min Cost Climbing Stairs
description: Problem Description and Solution for Min Cost Climbing Stairs
sidebar_label: 746. Min Cost Climbing Stairs
sidebar_position: 746
---

# [746. Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/)

```py title=min-cost-climbing-stairs.py
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        
        return min(dp[-1], dp[-2])
```


