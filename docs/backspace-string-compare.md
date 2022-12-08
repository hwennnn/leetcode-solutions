---
id: backspace-string-compare
title: Backspace String Compare
description: Problem Description and Solution for Backspace String Compare
sidebar_label: 844. Backspace String Compare
sidebar_position: 844
---

# [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

```py title=backspace-string-compare.py
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def check(A):
            stack = []
            
            for x in A:
                if x == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(x)
            
            return stack
        
        return check(s) == check(t)
```


