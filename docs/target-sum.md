---
id: target-sum
title: Target Sum
description: Problem Description and Solution for Target Sum
sidebar_label: 494. Target Sum
sidebar_position: 494
---

# [494. Target Sum](https://leetcode.com/problems/target-sum/)

```py title=target-sum.py
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        @cache
        def go(i, curr):
            if i == n and curr == target:
                return 1
            if i == n:
                return 0
            
            return go(i + 1, curr + nums[i]) + go(i + 1, curr - nums[i])
        
        return go(0, 0)
```


