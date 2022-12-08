---
id: number-of-arithmetic-triplets
title: Number of Arithmetic Triplets
description: Problem Description and Solution for Number of Arithmetic Triplets
sidebar_label: 2367. Number of Arithmetic Triplets
sidebar_position: 2367
---

# [2367. Number of Arithmetic Triplets](https://leetcode.com/problems/number-of-arithmetic-triplets/)

```py title=number-of-arithmetic-triplets.py
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        n = len(nums)
        res = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        res += 1
        
        return res
```


