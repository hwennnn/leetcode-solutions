---
id: pizza-with-3n-slices
title: Pizza With 3n Slices
description: Problem Description and Solution for Pizza With 3n Slices
sidebar_label: 1388. Pizza With 3n Slices
sidebar_position: 1388
---

# [1388. Pizza With 3n Slices](https://leetcode.com/problems/pizza-with-3n-slices/)

```py title=pizza-with-3n-slices.py
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        
        @cache
        def go(i, j, k):
            if k == 1: return max(slices[i : j + 1])
            
            if j - i + 1 < k * 2 - 1: return float('-inf')
            
            return max(go(i + 2, j, k - 1) + slices[i], go(i + 1, j, k))
        
        n = len(slices)
        
        return max(go(0, n - 2, n // 3), go(1, n - 1, n // 3))
```


