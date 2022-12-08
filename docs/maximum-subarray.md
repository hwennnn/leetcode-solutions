---
id: maximum-subarray
title: Maximum Subarray
description: Problem Description and Solution for Maximum Subarray
sidebar_label: 53. Maximum Subarray
sidebar_position: 53
---

# [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

```py title=maximum-subarray.py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = curr = nums[0]
        
        for x in nums[1:]:
            curr = max(curr + x, x)
            res = max(res, curr)
        
        return res
```


