---
id: shifting-letters
title: Shifting Letters
description: Problem Description and Solution for Shifting Letters
sidebar_label: 848. Shifting Letters
sidebar_position: 848
---

# [848. Shifting Letters](https://leetcode.com/problems/shifting-letters/)

```py title=shifting-letters.py
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        count = 0
        res = ''
        
        for i in range(n - 1, -1, -1):
            count += shifts[i]
            v = (ord(s[i]) - ord('a') + count) % 26
            res += chr(v + ord('a'))
        
        return res[::-1]
```


