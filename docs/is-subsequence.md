---
id: is-subsequence
title: Is Subsequence
description: Problem Description and Solution for Is Subsequence
sidebar_label: 392. Is Subsequence
sidebar_position: 392
---

# [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)

```py title=is-subsequence.py
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        i = 0
        
        for x in t:
            if i < n and x == s[i]:
                i += 1
            
            if i == n:
                break
        
        return i == n
```


