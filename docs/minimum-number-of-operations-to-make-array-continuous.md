---
id: minimum-number-of-operations-to-make-array-continuous
title: Minimum Number of Operations to Make Array Continuous
description: Problem Description and Solution for Minimum Number of Operations to Make Array Continuous
sidebar_label: 2009. Minimum Number of Operations to Make Array Continuous
sidebar_position: 2009
---

# [2009. Minimum Number of Operations to Make Array Continuous](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/)

```py title=minimum-number-of-operations-to-make-array-continuous.py
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        res = n
        
        for i, start in enumerate(nums):
            end = n - 1 + start
            index = bisect.bisect(nums, end)
            between = index - i
            res = min(res, n - between)
        
        return res
```


