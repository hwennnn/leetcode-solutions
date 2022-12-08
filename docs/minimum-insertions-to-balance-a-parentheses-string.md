---
id: minimum-insertions-to-balance-a-parentheses-string
title: Minimum Insertions to Balance a Parentheses String
description: Problem Description and Solution for Minimum Insertions to Balance a Parentheses String
sidebar_label: 1541. Minimum Insertions to Balance a Parentheses String
sidebar_position: 1541
---

# [1541. Minimum Insertions to Balance a Parentheses String](https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/)

```py title=minimum-insertions-to-balance-a-parentheses-string.py
class Solution:
    def minInsertions(self, s: str) -> int:
        res = closed = 0
        
        for c in s:
            if c == '(':
                if closed & 1:
                    closed -= 1
                    res += 1
                    
                closed += 2
            else:
                if closed == 0:
                    res += 1
                    closed += 2
                    
                closed -= 1
        
        return res + closed
```


