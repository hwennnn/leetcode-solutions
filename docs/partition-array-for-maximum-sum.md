---
id: partition-array-for-maximum-sum
title: Partition Array for Maximum Sum
description: Problem Description and Solution for Partition Array for Maximum Sum
sidebar_label: 1043. Partition Array for Maximum Sum
sidebar_position: 1043
---

# [1043. Partition Array for Maximum Sum](https://leetcode.com/problems/partition-array-for-maximum-sum/)

```py title=partition-array-for-maximum-sum.py
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        N = len(A)
        dp = [0] * (N + 1)
        
        for i in range(1, N + 1):
            mmax = 0
            for k in range(1, min(i, K) + 1):
                mmax = max(mmax, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + mmax * k)
        
        return dp[N]
```


