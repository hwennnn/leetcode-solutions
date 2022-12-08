---
id: find-closest-number-to-zero
title: Find Closest Number to Zero
description: Problem Description and Solution for Find Closest Number to Zero
sidebar_label: 2239. Find Closest Number to Zero
sidebar_position: 2239
---

# [2239. Find Closest Number to Zero](https://leetcode.com/problems/find-closest-number-to-zero/)

```py title=find-closest-number-to-zero.py
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        m = float('inf')
        
        for x in nums:
            if abs(x) < abs(m):
                m = x
            elif abs(x) == abs(m):
                m = max(m, x)
        
        return m
```


