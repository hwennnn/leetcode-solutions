---
id: running-sum-of-1d-array
title: Running Sum of 1d Array
description: Problem Description and Solution for Running Sum of 1d Array
sidebar_label: 1480. Running Sum of 1d Array
sidebar_position: 1480
---

# [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/)

```py title=running-sum-of-1d-array.py
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        return nums
```


