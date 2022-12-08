---
id: monotonic-array
title: Monotonic Array
description: Problem Description and Solution for Monotonic Array
sidebar_label: 896. Monotonic Array
sidebar_position: 896
---

# [896. Monotonic Array](https://leetcode.com/problems/monotonic-array/)

```py title=monotonic-array.py
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        inc = dec = 0
        
        for i in range(n - 1):
            if nums[i] <= nums[i + 1]:
                inc += 1
            
            if nums[i] >= nums[i + 1]:
                dec += 1
        
        return inc == n - 1 or dec == n - 1
```


