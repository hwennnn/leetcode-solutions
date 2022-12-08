---
id: maximum-sum-circular-subarray
title: Maximum Sum Circular Subarray
description: Problem Description and Solution for Maximum Sum Circular Subarray
sidebar_label: 918. Maximum Sum Circular Subarray
sidebar_position: 918
---

# [918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

```py title=maximum-sum-circular-subarray.py
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMin = mmin = currMax = mmax = total = nums[0]
        
        for i in range(1, len(nums)):
            total += nums[i]
            currMin = min(nums[i], currMin + nums[i])
            mmin = min(mmin, currMin)
            currMax = max(nums[i], currMax + nums[i])
            mmax = max(mmax, currMax)

        return max(mmax, total - mmin) if mmax > 0 else mmax
```


