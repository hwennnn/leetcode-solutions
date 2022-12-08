---
id: repeated-substring-pattern
title: Repeated Substring Pattern
description: Problem Description and Solution for Repeated Substring Pattern
sidebar_label: 459. Repeated Substring Pattern
sidebar_position: 459
---

# [459. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/)

```py title=repeated-substring-pattern.py
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s+s)[1:-1]
```


