---
id: append-characters-to-string-to-make-subsequence
title: Append Characters to String to Make Subsequence
description: Problem Description and Solution for Append Characters to String to Make Subsequence
sidebar_label: 2486. Append Characters to String to Make Subsequence
sidebar_position: 2486
---

# [2486. Append Characters to String to Make Subsequence](https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/)

```py title=append-characters-to-string-to-make-subsequence.py
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        j = 0
        curr = 0
        
        for i, x in enumerate(s):
            if j == M: break
                
            if x == t[j]:
                curr += 1
                j += 1
        
        return M - curr
                
```


