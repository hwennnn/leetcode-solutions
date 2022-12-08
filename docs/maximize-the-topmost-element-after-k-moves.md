---
id: maximize-the-topmost-element-after-k-moves
title: Maximize the Topmost Element After K Moves
description: Problem Description and Solution for Maximize the Topmost Element After K Moves
sidebar_label: 2202. Maximize the Topmost Element After K Moves
sidebar_position: 2202
---

# [2202. Maximize the Topmost Element After K Moves](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/)

```py title=maximize-the-topmost-element-after-k-moves.py
class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        if k == 0: return nums[0]
        
        if k == 1: return -1 if n == 1 else nums[1]
        
        if n == 1: return -1 if k & 1 else nums[0]
        
        mmax = max(nums[:min(n, k - 1)])
        
        if k < n:
            mmax = max(mmax, nums[k])
        
        return mmax
```


