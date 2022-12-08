---
id: merge-strings-alternately
title: Merge Strings Alternately
description: Problem Description and Solution for Merge Strings Alternately
sidebar_label: 1768. Merge Strings Alternately
sidebar_position: 1768
---

# [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/)

```py title=merge-strings-alternately.py
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        
        for a, b in zip_longest(word1, word2, fillvalue=""):
            res += a + b
        
        return res
```


