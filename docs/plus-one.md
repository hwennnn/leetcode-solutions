---
id: plus-one
title: Plus One
description: Problem Description and Solution for Plus One
sidebar_label: 66. Plus One
sidebar_position: 66
---

# [66. Plus One](https://leetcode.com/problems/plus-one/)

```py title=plus-one.py
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        digits[-1] += 1
        carry = 0
        
        for x in digits[::-1]:
            carry += x
            
            res.append(carry % 10)
            carry //= 10
        
        if carry > 0:
            res.append(carry)
        
        return res[::-1]
```


