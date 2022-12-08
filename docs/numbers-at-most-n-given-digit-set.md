---
id: numbers-at-most-n-given-digit-set
title: Numbers At Most N Given Digit Set
description: Problem Description and Solution for Numbers At Most N Given Digit Set
sidebar_label: 902. Numbers At Most N Given Digit Set
sidebar_position: 902
---

# [902. Numbers At Most N Given Digit Set](https://leetcode.com/problems/numbers-at-most-n-given-digit-set/)

```py title=numbers-at-most-n-given-digit-set.py
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        nStr = str(n)
        res = 0
        digits = list(map(int, digits))
        
        for i in range(1, len(nStr)):
            res += pow(len(digits), i)
        
        for i in range(len(nStr)):
            hasSameNumber = False
            
            for digit in digits:
                if digit < int(nStr[i]):
                    res += pow(len(digits), len(nStr) - i - 1)
                elif digit == int(nStr[i]):
                    hasSameNumber = True
            
            if not hasSameNumber: return res
        
        return res + 1
```


