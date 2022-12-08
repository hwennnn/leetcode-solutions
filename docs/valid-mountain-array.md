---
id: valid-mountain-array
title: Valid Mountain Array
description: Problem Description and Solution for Valid Mountain Array
sidebar_label: 941. Valid Mountain Array
sidebar_position: 941
---

# [941. Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)

```py title=valid-mountain-array.py
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False
        
        i, j = 0, n - 1
        
        while i + 1 < n and arr[i] < arr[i + 1]: 
            i += 1
        
        while j > 0 and arr[j] < arr[j - 1]:
            j -= 1
        
        return i == j and j != n - 1 and i != 0
```


