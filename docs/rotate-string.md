---
id: rotate-string
title: Rotate String
description: Problem Description and Solution for Rotate String
sidebar_label: 796. Rotate String
sidebar_position: 796
---

# [796. Rotate String](https://leetcode.com/problems/rotate-string/)

```py title=rotate-string.py
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        
        return len(A) == len(B) and B in A+A
```


