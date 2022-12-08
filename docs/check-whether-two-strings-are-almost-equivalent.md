---
id: check-whether-two-strings-are-almost-equivalent
title: Check Whether Two Strings are Almost Equivalent
description: Problem Description and Solution for Check Whether Two Strings are Almost Equivalent
sidebar_label: 2068. Check Whether Two Strings are Almost Equivalent
sidebar_position: 2068
---

# [2068. Check Whether Two Strings are Almost Equivalent](https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/)

```py title=check-whether-two-strings-are-almost-equivalent.py
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        for k1, v1 in counter1.items():
            if abs(counter2[k1] - v1) > 3:
                return False
        
        for k2, v2 in counter2.items():
            if abs(counter1[k2] - v2) > 3:
                return False
        
        return True
```


