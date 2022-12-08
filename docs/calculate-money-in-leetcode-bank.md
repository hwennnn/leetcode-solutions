---
id: calculate-money-in-leetcode-bank
title: Calculate Money in Leetcode Bank
description: Problem Description and Solution for Calculate Money in Leetcode Bank
sidebar_label: 1716. Calculate Money in Leetcode Bank
sidebar_position: 1716
---

# [1716. Calculate Money in Leetcode Bank](https://leetcode.com/problems/calculate-money-in-leetcode-bank/)

```py title=calculate-money-in-leetcode-bank.py
class Solution:
    def totalMoney(self, n: int) -> int:
        res = times = 0
        c = 1
        
        for _ in range(n):
            if c == 8: 
                c = 1
                times += 1
            
            res += c + times
            c += 1
            
        return res
```


