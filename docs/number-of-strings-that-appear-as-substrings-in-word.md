---
id: number-of-strings-that-appear-as-substrings-in-word
title: Number of Strings That Appear as Substrings in Word
description: Problem Description and Solution for Number of Strings That Appear as Substrings in Word
sidebar_label: 1967. Number of Strings That Appear as Substrings in Word
sidebar_position: 1967
---

# [1967. Number of Strings That Appear as Substrings in Word](https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/)

```py title=number-of-strings-that-appear-as-substrings-in-word.py
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        res = 0
        
        for p in patterns:
            if p in word:
                res += 1
        
        return res
```


