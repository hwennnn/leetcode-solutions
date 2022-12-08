---
id: add-digits
title: Add Digits
description: Problem Description and Solution for Add Digits
sidebar_label: 258. Add Digits
sidebar_position: 258
---

# [258. Add Digits](https://leetcode.com/problems/add-digits/)

```py title=add-digits.py
class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            s = 0
            
            while num > 0:
                s += num % 10
                num //= 10
            
            num = s
            
        return num
```


