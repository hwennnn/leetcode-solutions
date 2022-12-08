---
id: relative-sort-array
title: Relative Sort Array
description: Problem Description and Solution for Relative Sort Array
sidebar_label: 1122. Relative Sort Array
sidebar_position: 1122
---

# [1122. Relative Sort Array](https://leetcode.com/problems/relative-sort-array/)

```py title=relative-sort-array.py
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = collections.Counter(arr1) 
        s = set(arr2)
        res = []
        
        for num in arr2:
            res += [num] * mp[num]
        
        leftover = []
        for num in arr1:
            if num not in s:
                leftover.append(num)

        return res + sorted(leftover)
```


