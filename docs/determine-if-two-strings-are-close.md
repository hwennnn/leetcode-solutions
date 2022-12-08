---
id: determine-if-two-strings-are-close
title: Determine if Two Strings Are Close
description: Problem Description and Solution for Determine if Two Strings Are Close
sidebar_label: 1657. Determine if Two Strings Are Close
sidebar_position: 1657
---

# [1657. Determine if Two Strings Are Close](https://leetcode.com/problems/determine-if-two-strings-are-close/)

```py title=determine-if-two-strings-are-close.py
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2) and set(word1) == set(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values())
```


