---
id: maximum-score-from-performing-multiplication-operations
title: Maximum Score from Performing Multiplication Operations
description: Problem Description and Solution for Maximum Score from Performing Multiplication Operations
sidebar_label: 1770. Maximum Score from Performing Multiplication Operations
sidebar_position: 1770
---

# [1770. Maximum Score from Performing Multiplication Operations](https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/)

```py title=maximum-score-from-performing-multiplication-operations.py
class Solution:
    def maximumScore(self, nums: List[int], mul: List[int]) -> int:
        dp = [0] * (len(mul) + 1)
        
        for m in range(len(mul) - 1, -1, -1):
            pd = [0] * (m + 1)
            for l in range(m, -1, -1):
                pd[l] = max(dp[l + 1] + mul[m] * nums[l], 
                            dp[l] + mul[m] * nums[~(m - l)])
            dp = pd
            
        return dp[0]
```


