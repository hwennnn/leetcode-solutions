---
id: number-of-zero-filled-subarrays
title: Number of Zero-Filled Subarrays
description: Problem Description and Solution for Number of Zero-Filled Subarrays
sidebar_label: 2348. Number of Zero-Filled Subarrays
sidebar_position: 2348
---

# [2348. Number of Zero-Filled Subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays/)

```py title=number-of-zero-filled-subarrays.py
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = curr = 0
        
        for x in nums:
            if x != 0:
                curr = 0
            else:
                curr += 1
                res += curr
        
        return res
```


