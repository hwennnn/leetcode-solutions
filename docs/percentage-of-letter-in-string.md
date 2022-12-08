---
id: percentage-of-letter-in-string
title: Percentage of Letter in String
description: Problem Description and Solution for Percentage of Letter in String
sidebar_label: 2278. Percentage of Letter in String
sidebar_position: 2278
---

# [2278. Percentage of Letter in String](https://leetcode.com/problems/percentage-of-letter-in-string/)

```py title=percentage-of-letter-in-string.py
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        c = s.count(letter)
        # print(n, c)
        return int(c / n * 100)
```


