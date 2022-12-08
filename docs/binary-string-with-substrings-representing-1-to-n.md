---
id: binary-string-with-substrings-representing-1-to-n
title: Binary String With Substrings Representing 1 To N
description: Problem Description and Solution for Binary String With Substrings Representing 1 To N
sidebar_label: 1016. Binary String With Substrings Representing 1 To N
sidebar_position: 1016
---

# [1016. Binary String With Substrings Representing 1 To N](https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/)

```py title=binary-string-with-substrings-representing-1-to-n.py
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        
        for i in range(n // 2 + 1, n + 1):
            b = bin(i)[2:]
            if b not in s: return False
        
        return True
```


