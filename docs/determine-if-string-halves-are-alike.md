---
id: determine-if-string-halves-are-alike
title: Determine if String Halves Are Alike
description: Problem Description and Solution for Determine if String Halves Are Alike
sidebar_label: 1704. Determine if String Halves Are Alike
sidebar_position: 1704
---

# [1704. Determine if String Halves Are Alike](https://leetcode.com/problems/determine-if-string-halves-are-alike/)

```py title=determine-if-string-halves-are-alike.py
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s)
        first = second = 0
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])

        for i in range(N):
            if s[i] in vowels:
                if i < N // 2:
                    first += 1
                else:
                    second += 1

        return first == second
```


