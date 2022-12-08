---
id: number-of-subarrays-with-bounded-maximum
title: Number of Subarrays with Bounded Maximum
description: Problem Description and Solution for Number of Subarrays with Bounded Maximum
sidebar_label: 795. Number of Subarrays with Bounded Maximum
sidebar_position: 795
---

# [795. Number of Subarrays with Bounded Maximum](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/)

```py title=number-of-subarrays-with-bounded-maximum.py
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        res = dp = 0
        prev = -1
        
        for i,x in enumerate(nums):
            if i > 0 and x < left:
                res += dp
            
            if x > right:
                prev = i
                dp = 0
            
            if left <= x <= right:
                dp = i - prev
                res += dp
        
        return res
```


