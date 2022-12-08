---
id: ways-to-make-a-fair-array
title: Ways to Make a Fair Array
description: Problem Description and Solution for Ways to Make a Fair Array
sidebar_label: 1664. Ways to Make a Fair Array
sidebar_position: 1664
---

# [1664. Ways to Make a Fair Array](https://leetcode.com/problems/ways-to-make-a-fair-array/)

```py title=ways-to-make-a-fair-array.py
class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ro = re = 0
        for i,x in enumerate(nums):
            if i & 1: ro += x
            else: re += x
        
        lo = le = res = 0
        for i,x in enumerate(nums):
            if i & 1: ro -= x
            else: re -= x
            
            res += (lo + re) == (le + ro)
            
            if i & 1: lo += x
            else: le += x
        
        return res
```


