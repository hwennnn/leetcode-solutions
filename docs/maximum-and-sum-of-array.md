---
id: maximum-and-sum-of-array
title: Maximum AND Sum of Array
description: Problem Description and Solution for Maximum AND Sum of Array
sidebar_label: 2172. Maximum AND Sum of Array
sidebar_position: 2172
---

# [2172. Maximum AND Sum of Array](https://leetcode.com/problems/maximum-and-sum-of-array/)

```py title=maximum-and-sum-of-array.py
class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        n = len(nums)
        
        @cache
        def go(index, slots):
            if index == n:
                return 0
            
            res = 0
                
            for slot in range(numSlots):
                if slots & (1 << (slot * 2)) > 0 and slots & (1 << (slot * 2 + 1)) > 0: continue

                y = nums[index] & (slot + 1)

                if slots & (1 << (slot * 2)) == 0:
                    res = max(res, y + go(index + 1, slots ^ (1 << (slot * 2))))
                else:
                    res = max(res, y + go(index + 1, slots ^ (1 << (slot * 2 + 1))))
            
            return res
        
        return go(0, 0)
```


