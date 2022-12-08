---
id: check-if-one-string-swap-can-make-strings-equal
title: Check if One String Swap Can Make Strings Equal
description: Problem Description and Solution for Check if One String Swap Can Make Strings Equal
sidebar_label: 1790. Check if One String Swap Can Make Strings Equal
sidebar_position: 1790
---

# [1790. Check if One String Swap Can Make Strings Equal](https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/)

```py title=check-if-one-string-swap-can-make-strings-equal.py
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2: return True
        diff = 0
        
        for a, b in zip(s1, s2):
            if a != b:
                diff += 1
        
        return diff == 2 and Counter(s1) == Counter(s2)
```


