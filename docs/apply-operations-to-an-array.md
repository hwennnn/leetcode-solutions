---
id: apply-operations-to-an-array
title: Apply Operations to an Array
description: Problem Description and Solution for Apply Operations to an Array
sidebar_label: 2460. Apply Operations to an Array
sidebar_position: 2460
---

# [2460. Apply Operations to an Array](https://leetcode.com/problems/apply-operations-to-an-array/)

```py title=apply-operations-to-an-array.py
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
      
        i = 0
        for x in nums:
            if x != 0:
                nums[i] = x
                i += 1

        for k in range(i, N):
            nums[k] = 0
        
        return nums
```


