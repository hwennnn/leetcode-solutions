---
id: check-if-a-parentheses-string-can-be-valid
title: Check if a Parentheses String Can Be Valid
description: Problem Description and Solution for Check if a Parentheses String Can Be Valid
sidebar_label: 2116. Check if a Parentheses String Can Be Valid
sidebar_position: 2116
---

# [2116. Check if a Parentheses String Can Be Valid](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/)

```py title=check-if-a-parentheses-string-can-be-valid.py
class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        s = list(s)
        
        if n & 1: return False
        
        for i in range(n):
            if locked[i] == '0':
                s[i] = '#'
        
        opened = closed = 0
        for x in s:
            if x == '#' or x == '(':
                opened += 1
            else:
                closed += 1
            
            if closed > opened:
                return False
        
        opened = closed = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '#' or s[i] == ')':
                closed += 1
            else:
                opened += 1
            
            if opened > closed:
                return False
        
        return True
```


