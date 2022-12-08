---
id: partition-array-such-that-maximum-difference-is-k
title: Partition Array Such That Maximum Difference Is K
description: Problem Description and Solution for Partition Array Such That Maximum Difference Is K
sidebar_label: 2294. Partition Array Such That Maximum Difference Is K
sidebar_position: 2294
---

# [2294. Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/)

```py title=partition-array-such-that-maximum-difference-is-k.py
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        res = 1
        mmin = mmax = nums[0]
        
        for i in range(1, n):
            if nums[i] > mmax:
                mmax = nums[i]
            
            if nums[i] < mmin:
                mmin = nums[i]
            
            if mmax - mmin > k:
                res += 1
                mmax = mmin = nums[i]
        
        return res
```


