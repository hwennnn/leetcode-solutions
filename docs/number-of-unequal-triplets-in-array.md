---
id: number-of-unequal-triplets-in-array
title: Number of Unequal Triplets in Array
description: Problem Description and Solution for Number of Unequal Triplets in Array
sidebar_label: 2475. Number of Unequal Triplets in Array
sidebar_position: 2475
---

# [2475. Number of Unequal Triplets in Array](https://leetcode.com/problems/number-of-unequal-triplets-in-array/)

```py title=number-of-unequal-triplets-in-array.py
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        res += 1
        
        return res
```


