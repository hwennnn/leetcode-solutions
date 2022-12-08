---
id: roman-to-integer
title: Roman to Integer
description: Problem Description and Solution for Roman to Integer
sidebar_label: 13. Roman to Integer
sidebar_position: 13
---

# [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

```py title=roman-to-integer.py
class Solution:
    def romanToInt(self, s: str):
        
        mp = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        prev = 0
        total = 0
        
        for i in s[::-1]:
            curr = mp[i]
            if prev > curr:
                total -= curr
            else:
                total += curr
            prev = curr
            
        return total
```


