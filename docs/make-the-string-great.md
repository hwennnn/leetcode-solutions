---
id: make-the-string-great
title: Make The String Great
description: Problem Description and Solution for Make The String Great
sidebar_label: 1544. Make The String Great
sidebar_position: 1544
---

# [1544. Make The String Great](https://leetcode.com/problems/make-the-string-great/)

```py title=make-the-string-great.py
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        
        for x in s:
            stack.append(x)
            while len(stack) >= 2 and stack[-1] != stack[-2] and stack[-1].upper() == stack[-2].upper():
                stack.pop()
                stack.pop()
        
        return "".join(stack)
            
```


