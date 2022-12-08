---
id: build-array-from-permutation
title: Build Array from Permutation
description: Problem Description and Solution for Build Array from Permutation
sidebar_label: 1920. Build Array from Permutation
sidebar_position: 1920
---

# [1920. Build Array from Permutation](https://leetcode.com/problems/build-array-from-permutation/)

```py title=build-array-from-permutation.py
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = nums[nums[i]]
        
        return res
```


