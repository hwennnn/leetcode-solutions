---
id: number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers
title: Number of Ways Where Square of Number Is Equal to Product of Two Numbers
description: Problem Description and Solution for Number of Ways Where Square of Number Is Equal to Product of Two Numbers
sidebar_label: 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
sidebar_position: 1577
---

# [1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers](https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/)

```py title=number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers.py
from collections import Counter
class Solution:
    def numTriplets(self, A: List[int], B: List[int]) -> int:
        countA = Counter()
        countB = Counter()
        res = 0
        
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                countA[A[i]*A[j]] += 1
        
        for i in range(len(B)):
            for j in range(i+1, len(B)):
                countB[B[i]*B[j]] += 1

        for num in A:
            res += countB[num*num]
        
        for num in B:
            res += countA[num*num]
        
        return res
        
```


