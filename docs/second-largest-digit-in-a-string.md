---
id: second-largest-digit-in-a-string
title: Second Largest Digit in a String
description: Problem Description and Solution for Second Largest Digit in a String
sidebar_label: 1796. Second Largest Digit in a String
sidebar_position: 1796
---

# [1796. Second Largest Digit in a String](https://leetcode.com/problems/second-largest-digit-in-a-string/)

```py title=second-largest-digit-in-a-string.py
class Solution:
    def secondHighest(self, s: str) -> int:
        res = set(list(c for c in s if c.isdigit()))
    
        return sorted(list(res))[-2] if len(res) > 1 else -1
```


