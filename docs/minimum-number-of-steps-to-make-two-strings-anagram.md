---
id: minimum-number-of-steps-to-make-two-strings-anagram
title: Minimum Number of Steps to Make Two Strings Anagram
description: Problem Description and Solution for Minimum Number of Steps to Make Two Strings Anagram
sidebar_label: 1347. Minimum Number of Steps to Make Two Strings Anagram
sidebar_position: 1347
---

# [1347. Minimum Number of Steps to Make Two Strings Anagram](https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/)

```py title=minimum-number-of-steps-to-make-two-strings-anagram.py
class Solution:
    def minSteps(self, S: str, T: str) -> int:
        s = collections.Counter(S)
        t = collections.Counter(T)
        
        for k in s:
            if k in t:
                s[k] = max(0,s[k]-t[k])
        
        res = 0
        for v in s.values():
            res += v
            
        return res
```


