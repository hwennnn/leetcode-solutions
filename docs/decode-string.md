---
id: decode-string
title: Decode String
description: Problem Description and Solution for Decode String
sidebar_label: 394. Decode String
sidebar_position: 394
---

# [394. Decode String](https://leetcode.com/problems/decode-string/)

```py title=decode-string.py
class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        
        for x in s:
            if x == ']':
                chars = ""
                
                while stack and stack[-1] != '[':
                    chars = stack.pop() + chars
                
                stack.pop()
                
                times = ""
                
                while stack and stack[-1].isnumeric():
                    times = stack.pop() + times
                
                stack.append(int(times) * chars)  
            else:
                stack.append(x)
        
        return "".join(stack)
```


