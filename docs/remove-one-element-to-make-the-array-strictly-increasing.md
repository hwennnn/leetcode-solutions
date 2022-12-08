---
id: remove-one-element-to-make-the-array-strictly-increasing
title: Remove One Element to Make the Array Strictly Increasing
description: Problem Description and Solution for Remove One Element to Make the Array Strictly Increasing
sidebar_label: 1909. Remove One Element to Make the Array Strictly Increasing
sidebar_position: 1909
---

# [1909. Remove One Element to Make the Array Strictly Increasing](https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/)

```py title=remove-one-element-to-make-the-array-strictly-increasing.py
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        
        def isIncreasing(A):
            for i in range(1, len(A)):
                if A[i] <= A[i - 1]: return False
            
            return True
        
        for i in range(len(nums)):
            if isIncreasing(nums[:i] + nums[i + 1:]): return True
            
        return False
```


