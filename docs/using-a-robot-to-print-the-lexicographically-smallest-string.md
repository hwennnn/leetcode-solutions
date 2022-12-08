---
id: using-a-robot-to-print-the-lexicographically-smallest-string
title: Using a Robot to Print the Lexicographically Smallest String
description: Problem Description and Solution for Using a Robot to Print the Lexicographically Smallest String
sidebar_label: 2434. Using a Robot to Print the Lexicographically Smallest String
sidebar_position: 2434
---

# [2434. Using a Robot to Print the Lexicographically Smallest String](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/)

```py title=using-a-robot-to-print-the-lexicographically-smallest-string.py
class Solution:
    def robotWithString(self, s: str) -> str:
        N = len(s)
        res = []
        stack = []
        count = Counter(s)
        
        for x in s:
            stack.append(x)
            
            if count[x] == 1:
                del count[x]
            else:
                count[x] -= 1
            
            while stack and count and stack[-1] <= min(count):
                res.append(stack.pop())
        
        if stack:
            res += stack[::-1]
        
        return "".join(res)
```


