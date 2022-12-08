---
id: minimum-increment-to-make-array-unique
title: Minimum Increment to Make Array Unique
description: Problem Description and Solution for Minimum Increment to Make Array Unique
sidebar_label: 945. Minimum Increment to Make Array Unique
sidebar_position: 945
---

# [945. Minimum Increment to Make Array Unique](https://leetcode.com/problems/minimum-increment-to-make-array-unique/)

```py title=minimum-increment-to-make-array-unique.py
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        nums.sort()
        
        for i, x in enumerate(nums):
            if i > 0 and nums[i] <= nums[i - 1]:
                res += nums[i - 1] - nums[i] + 1
                nums[i] += nums[i - 1] - nums[i] + 1
            
        return res
        
```


