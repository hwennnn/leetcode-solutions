---
id: find-pivot-index
title: Find Pivot Index
description: Problem Description and Solution for Find Pivot Index
sidebar_label: 724. Find Pivot Index
sidebar_position: 724
---

# [724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

```py title=find-pivot-index.py
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        s = 0
        
        for i, x in enumerate(nums):
            total -= x
            
            if s == total:
                return i
            
            s += x

            
        return -1
```


