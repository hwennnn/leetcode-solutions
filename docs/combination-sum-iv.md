---
id: combination-sum-iv
title: Combination Sum IV
description: Problem Description and Solution for Combination Sum IV
sidebar_label: 377. Combination Sum IV
sidebar_position: 377
---

# [377. Combination Sum IV](https://leetcode.com/problems/combination-sum-iv/)

```py title=combination-sum-iv.py
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        
        for t in range(1, target + 1):
            for x in nums:
                if x > t: break
                dp[t] += dp[t - x]
        
        return dp[target]
```


