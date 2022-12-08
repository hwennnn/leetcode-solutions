---
id: longest-nice-subarray
title: Longest Nice Subarray
description: Problem Description and Solution for Longest Nice Subarray
sidebar_label: 2401. Longest Nice Subarray
sidebar_position: 2401
---

# [2401. Longest Nice Subarray](https://leetcode.com/problems/longest-nice-subarray/)

```py title=longest-nice-subarray.py
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 1
        i = mask = 0
        
        for j, x in enumerate(nums):
            while mask & x != 0:
                mask ^= (nums[i])
                i += 1
                
            mask |= x
            res = max(res, j - i + 1)
        
        return res
```


