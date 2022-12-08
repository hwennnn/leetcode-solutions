---
id: add-to-array-form-of-integer
title: Add to Array-Form of Integer
description: Problem Description and Solution for Add to Array-Form of Integer
sidebar_label: 989. Add to Array-Form of Integer
sidebar_position: 989
---

# [989. Add to Array-Form of Integer](https://leetcode.com/problems/add-to-array-form-of-integer/)

```py title=add-to-array-form-of-integer.py
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        carry = 0
        res = []
        
        for x in num[::-1]:
            carry += x + k % 10
            k //= 10
            
            res.append(carry % 10)
            carry //= 10
        
        while k > 0 or carry > 0:
            carry += k % 10
            k //= 10
            
            res.append(carry % 10)
            carry //= 10
        
        return res[::-1]
```


