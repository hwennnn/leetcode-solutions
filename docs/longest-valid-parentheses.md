---
id: longest-valid-parentheses
title: Longest Valid Parentheses
description: Problem Description and Solution for Longest Valid Parentheses
sidebar_label: 32. Longest Valid Parentheses
sidebar_position: 32
---

# [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

```py title=longest-valid-parentheses.py
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        opened = []
        mp = [False] * n
        
        for i, c in enumerate(s):
            if c == "(":
                opened.append(i)
            else:
                if opened:
                    mp[opened.pop()] = True
                    mp[i] = True
        
        res = total = i = 0
        while i < n:
            if i + 1 < n and mp[i] and mp[i+1]:
                total += 2
                i += 2
            else:
                total = 0
                i += 1
            
            res = max(res, total)
    
        return res
                    
```


