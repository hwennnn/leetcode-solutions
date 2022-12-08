---
id: sum-of-all-odd-length-subarrays
title: Sum of All Odd Length Subarrays
description: Problem Description and Solution for Sum of All Odd Length Subarrays
sidebar_label: 1588. Sum of All Odd Length Subarrays
sidebar_position: 1588
---

# [1588. Sum of All Odd Length Subarrays](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/)

```py title=sum-of-all-odd-length-subarrays.py
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        
        for i, x in enumerate(arr):
            res += x * math.ceil(((i + 1) * (n - i)) / 2)
        
        return res
```


