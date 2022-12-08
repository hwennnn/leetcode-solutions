---
id: maximum-number-of-points-with-cost
title: Maximum Number of Points with Cost
description: Problem Description and Solution for Maximum Number of Points with Cost
sidebar_label: 1937. Maximum Number of Points with Cost
sidebar_position: 1937
---

# [1937. Maximum Number of Points with Cost](https://leetcode.com/problems/maximum-number-of-points-with-cost/)

```py title=maximum-number-of-points-with-cost.py
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])
        dp = copy.deepcopy(points)
        
        for i in range(rows):
            for j in range(cols):
                if i >= 1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + points[i][j])

            for j in range(1, cols):
                dp[i][j] = max(dp[i][j], dp[i][j - 1] - 1)

            for j in range(cols - 2, -1, -1):
                dp[i][j] = max(dp[i][j], dp[i][j + 1] - 1)
        
        return max(dp[-1])
                
```


