---
id: maximum-absolute-sum-of-any-subarray
title: Maximum Absolute Sum of Any Subarray
description: Problem Description and Solution for Maximum Absolute Sum of Any Subarray
sidebar_label: 1749. Maximum Absolute Sum of Any Subarray
sidebar_position: 1749
---

# [1749. Maximum Absolute Sum of Any Subarray](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/)

```py title=maximum-absolute-sum-of-any-subarray.py
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mmax = mmin = s = 0
        
        for num in nums:
            s += num
            mmax = max(mmax, s)
            mmin = min(mmin, s)

        return mmax - mmin
```


