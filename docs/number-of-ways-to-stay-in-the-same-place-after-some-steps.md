---
id: number-of-ways-to-stay-in-the-same-place-after-some-steps
title: Number of Ways to Stay in the Same Place After Some Steps
description: Problem Description and Solution for Number of Ways to Stay in the Same Place After Some Steps
sidebar_label: 1269. Number of Ways to Stay in the Same Place After Some Steps
sidebar_position: 1269
---

# [1269. Number of Ways to Stay in the Same Place After Some Steps](https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/)

```py title=number-of-ways-to-stay-in-the-same-place-after-some-steps.py
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        M = 10 ** 9 + 7
        maxPos = min(steps, arrLen)
        
        dp = [[0]*(maxPos+1) for _ in range(steps+1)]
        dp[1][0] = 1
        dp[1][1] = 1
        
        for i in range(2, steps+1):
            for j in range(maxPos):
                stay = dp[i-1][j]
                left = dp[i-1][j-1] if j > 0 else 0
                right = dp[i-1][j+1]

                dp[i][j] = stay + left + right
            

        return dp[steps][0] % M
```


