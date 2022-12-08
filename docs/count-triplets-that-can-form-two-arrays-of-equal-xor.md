---
id: count-triplets-that-can-form-two-arrays-of-equal-xor
title: Count Triplets That Can Form Two Arrays of Equal XOR
description: Problem Description and Solution for Count Triplets That Can Form Two Arrays of Equal XOR
sidebar_label: 1442. Count Triplets That Can Form Two Arrays of Equal XOR
sidebar_position: 1442
---

# [1442. Count Triplets That Can Form Two Arrays of Equal XOR](https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/)

```py title=count-triplets-that-can-form-two-arrays-of-equal-xor.py
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            x = arr[i]
            for j in range(i+1, len(arr)):
                x ^= arr[j]
                if x == 0:
                    res += (j - i)
        
        return res
```


