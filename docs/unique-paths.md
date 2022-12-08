---
id: unique-paths
title: Unique Paths
description: Problem Description and Solution for Unique Paths
sidebar_label: 62. Unique Paths
sidebar_position: 62
---

# [62. Unique Paths](https://leetcode.com/problems/unique-paths/)

```py title=unique-paths.py
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        
        for i in range(m):
            dp[i][0] = 1
        
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += dp[i - 1][j] + dp[i][j - 1]
        
        return dp[-1][-1]
```


