---
id: sort-even-and-odd-indices-independently
title: Sort Even and Odd Indices Independently
description: Problem Description and Solution for Sort Even and Odd Indices Independently
sidebar_label: 2164. Sort Even and Odd Indices Independently
sidebar_position: 2164
---

# [2164. Sort Even and Odd Indices Independently](https://leetcode.com/problems/sort-even-and-odd-indices-independently/)

```py title=sort-even-and-odd-indices-independently.py
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        n = len(nums)
        odd, even = [], []
        
        for i, x in enumerate(nums):
            if i & 1:
                odd.append(x)
            else:
                even.append(x)
        
        odd.sort(key = lambda x: -x)
        even.sort()
        
        res = [-1] * n
        index = 0
        
        for i in range(0, n, 2):
            res[i] = even[index]
            index += 1
        
        index = 0
        
        for i in range(1, n, 2):
            res[i] = odd[index]
            index += 1
        
        return res
```


