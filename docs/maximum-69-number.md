---
id: maximum-69-number
title: Maximum 69 Number
description: Problem Description and Solution for Maximum 69 Number
sidebar_label: 1323. Maximum 69 Number
sidebar_position: 1323
---

# [1323. Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/)

```py title=maximum-69-number.py
class Solution:
    def maximum69Number (self, num: int) -> int:
        k = -1
        p = 0
        curr = num
        
        while curr > 0:
            d = curr % 10
            if d == 6:
                k = p
                
            p += 1  
            curr //= 10
         
        if k == -1: return num
        
        return num + 3 * 10 ** k
```


