---
id: count-special-integers
title: Count Special Integers
description: Problem Description and Solution for Count Special Integers
sidebar_label: 2376. Count Special Integers
sidebar_position: 2376
---

# [2376. Count Special Integers](https://leetcode.com/problems/count-special-integers/)

```py title=count-special-integers.py
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits.reverse()

        N = len(digits)

        @cache
        def dp(pos, tight, mask):
            if pos == N:
                return 1 if mask != 0 else 0
            
            limit = digits[pos] if tight else 9
            res = 0
            
            for i in range(0, limit + 1):
                if mask & (1 << i) > 0: continue
            
                nextTight = tight and i == digits[pos]
                nextMask = mask if i == 0 and mask == 0 else mask ^ (1 << i)
                
                res += dp(pos + 1, nextTight, nextMask)
                
            return res
    
        return dp(0, True, 0)
                
                
```


