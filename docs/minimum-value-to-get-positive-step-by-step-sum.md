---
id: minimum-value-to-get-positive-step-by-step-sum
title: Minimum Value to Get Positive Step by Step Sum
description: Problem Description and Solution for Minimum Value to Get Positive Step by Step Sum
sidebar_label: 1413. Minimum Value to Get Positive Step by Step Sum
sidebar_position: 1413
---

# [1413. Minimum Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/)

```py title=minimum-value-to-get-positive-step-by-step-sum.py
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        mmin = curr = 0
        
        for x in nums:
            curr += x
            mmin = min(mmin, curr)
        
        return mmin if mmin > 0 else abs(mmin) + 1
```


