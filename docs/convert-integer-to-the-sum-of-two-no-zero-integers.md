---
id: convert-integer-to-the-sum-of-two-no-zero-integers
title: Convert Integer to the Sum of Two No-Zero Integers
description: Problem Description and Solution for Convert Integer to the Sum of Two No-Zero Integers
sidebar_label: 1317. Convert Integer to the Sum of Two No-Zero Integers
sidebar_position: 1317
---

# [1317. Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/)

```py title=convert-integer-to-the-sum-of-two-no-zero-integers.py
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        
        def findZeroes(n):
            return str(n).count("0") > 0
        
        a, b = 1, n - 1
        
        while findZeroes(a) or findZeroes(b):
            if findZeroes(a):
                a += 1
                b -= 1
            if findZeroes(b):
                a += 1
                b -= 1
        
        return [a,b]
            
        
```


