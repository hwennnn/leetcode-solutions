---
id: count-substrings-that-differ-by-one-character
title: Count Substrings That Differ by One Character
description: Problem Description and Solution for Count Substrings That Differ by One Character
sidebar_label: 1638. Count Substrings That Differ by One Character
sidebar_position: 1638
---

# [1638. Count Substrings That Differ by One Character](https://leetcode.com/problems/count-substrings-that-differ-by-one-character/)

```py title=count-substrings-that-differ-by-one-character.py
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        if s == t: return 0

        res = 0
        for i in range(len(s)):
            for z in range(i+1):
                c1 = s[i-z:i+1]
                l = len(c1)
                for j in range(len(t)-l+1):
                    c2 = t[j:j+l]
                    if c1 != c2 and len(c1) == len(c2) and sum(c1[i] != c2[i] for i in range(l)) == 1:
                        res += 1
            
        return res
```


