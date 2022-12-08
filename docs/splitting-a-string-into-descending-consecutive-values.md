---
id: splitting-a-string-into-descending-consecutive-values
title: Splitting a String Into Descending Consecutive Values
description: Problem Description and Solution for Splitting a String Into Descending Consecutive Values
sidebar_label: 1849. Splitting a String Into Descending Consecutive Values
sidebar_position: 1849
---

# [1849. Splitting a String Into Descending Consecutive Values](https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/)

```py title=splitting-a-string-into-descending-consecutive-values.py
class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        
        def go(i, prev):
            if i == n: return True
            
            valid = False
            
            for j in range(i + 1, n + 1):
                if int(s[i : j]) == prev - 1:
                    valid |= go(j, prev - 1)
                
                if valid: return True
            
            return valid
        
        
        for i in range(1, n):
            if go(i, int(s[:i])):
                return True
        
        return False
        
```


