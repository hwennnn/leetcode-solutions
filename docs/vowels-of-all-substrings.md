---
id: vowels-of-all-substrings
title: Vowels of All Substrings
description: Problem Description and Solution for Vowels of All Substrings
sidebar_label: 2063. Vowels of All Substrings
sidebar_position: 2063
---

# [2063. Vowels of All Substrings](https://leetcode.com/problems/vowels-of-all-substrings/)

```py title=vowels-of-all-substrings.py
class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        res = 0

        for i, s in enumerate(word):
            if s == "a" or s == "e" or s == "i" or s == "o" or s == "u":
                res += ((n - i) * (i + 1))           

        return res
```


