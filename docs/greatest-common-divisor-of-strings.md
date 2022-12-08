---
id: greatest-common-divisor-of-strings
title: Greatest Common Divisor of Strings
description: Problem Description and Solution for Greatest Common Divisor of Strings
sidebar_label: 1071. Greatest Common Divisor of Strings
sidebar_position: 1071
---

# [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings/)

```py title=greatest-common-divisor-of-strings.py
class Solution:
    def gcdOfStrings(self, A: str, B: str) -> str:
        if len(A) == len(B):
            return A if A == B else ""
        
        if len(A) < len(B):
            A, B = B, A
        
        if A[:len(B)] == B:
            return self.gcdOfStrings(A[len(B):], B)
        else:
            return ""
```


