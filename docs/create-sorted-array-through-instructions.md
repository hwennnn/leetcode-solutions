---
id: create-sorted-array-through-instructions
title: Create Sorted Array through Instructions
description: Problem Description and Solution for Create Sorted Array through Instructions
sidebar_label: 1649. Create Sorted Array through Instructions
sidebar_position: 1649
---

# [1649. Create Sorted Array through Instructions](https://leetcode.com/problems/create-sorted-array-through-instructions/)

```py title=create-sorted-array-through-instructions.py
from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        M = 10 ** 9 + 7
        arr = SortedList()
        
        res = 0
        
        for num in instructions:
            l = arr.bisect_left(num)
            r = arr.bisect_right(num)
            
            res += min(l, len(arr) - r)
            res %= M
            arr.add(num)
        
        return res % M
```


