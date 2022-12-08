---
id: count-subarrays-with-fixed-bounds
title: Count Subarrays With Fixed Bounds
description: Problem Description and Solution for Count Subarrays With Fixed Bounds
sidebar_label: 2444. Count Subarrays With Fixed Bounds
sidebar_position: 2444
---

# [2444. Count Subarrays With Fixed Bounds](https://leetcode.com/problems/count-subarrays-with-fixed-bounds/)

```py title=count-subarrays-with-fixed-bounds.py
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        res = 0
        minPos = maxPos = -1
        i = 0
        
        for j, x in enumerate(nums):
            if x == minK:
                minPos = j
                
            if x == maxK:
                maxPos = j
            
            if x > maxK or x < minK:
                i = j + 1
            
            res += max(0, min(minPos, maxPos) - i + 1)
        
        return res
```


