---
id: maximum-erasure-value
title: Maximum Erasure Value
description: Problem Description and Solution for Maximum Erasure Value
sidebar_label: 1695. Maximum Erasure Value
sidebar_position: 1695
---

# [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

```py title=maximum-erasure-value.py
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        i = total = res = 0
        
        for j, x in enumerate(nums):
            while x in s:
                total -= nums[i]
                s.remove(nums[i])
                i += 1
                
            total += x
            s.add(x)
            res = max(res, total)
        
        return res
```


