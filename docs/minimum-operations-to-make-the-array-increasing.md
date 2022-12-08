---
id: minimum-operations-to-make-the-array-increasing
title: Minimum Operations to Make the Array Increasing
description: Problem Description and Solution for Minimum Operations to Make the Array Increasing
sidebar_label: 1827. Minimum Operations to Make the Array Increasing
sidebar_position: 1827
---

# [1827. Minimum Operations to Make the Array Increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/)

```py title=minimum-operations-to-make-the-array-increasing.py
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                d = nums[i - 1] + 1
                res += d - nums[i]
                nums[i] = d
    
        return res
```


