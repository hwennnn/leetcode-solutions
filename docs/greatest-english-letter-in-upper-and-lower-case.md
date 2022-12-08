---
id: greatest-english-letter-in-upper-and-lower-case
title: Greatest English Letter in Upper and Lower Case
description: Problem Description and Solution for Greatest English Letter in Upper and Lower Case
sidebar_label: 2309. Greatest English Letter in Upper and Lower Case
sidebar_position: 2309
---

# [2309. Greatest English Letter in Upper and Lower Case](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/)

```py title=greatest-english-letter-in-upper-and-lower-case.py
class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        
        for j in range(25, -1, -1):
            if chr(ord("a") + j) in s and chr(ord("A") + j) in s:
                return chr(ord("A") + j)
        
        return ""
```


