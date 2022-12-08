---
id: ugly-number-iii
title: Ugly Number III
description: Problem Description and Solution for Ugly Number III
sidebar_label: 1201. Ugly Number III
sidebar_position: 1201
---

# [1201. Ugly Number III](https://leetcode.com/problems/ugly-number-iii/)

```py title=ugly-number-iii.py
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        
        def enough(x):
            total = (x // a) + (x // b) + (x // c) - (x // ab) - (x // bc) - (x // ac) + (x // abc)
            return total >= n
            
        ab = a*b // math.gcd(a,b)
        bc = b*c // math.gcd(b,c)
        ac = a*c // math.gcd(a,c)
        abc = a*bc // math.gcd(a,bc)
        
        left, right = 1, 10 ** 10
        while left < right:
            mid = left + (right-left) // 2
            
            if enough(mid):
                right = mid
            else:
                left = mid + 1
            
        return left
```


