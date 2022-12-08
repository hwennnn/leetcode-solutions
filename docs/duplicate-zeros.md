---
id: duplicate-zeros
title: Duplicate Zeros
description: Problem Description and Solution for Duplicate Zeros
sidebar_label: 1089. Duplicate Zeros
sidebar_position: 1089
---

# [1089. Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/)

```py title=duplicate-zeros.py
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        zeroes = arr.count(0)
        n = len(arr)
        
        for i in range(n - 1, -1, -1):
            
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            
            if arr[i] == 0:
                zeroes -= 1
                
                if i + zeroes < n:
                    arr[i + zeroes] = 0
```


