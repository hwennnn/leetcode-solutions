---
id: maximize-number-of-subsequences-in-a-string
title: Maximize Number of Subsequences in a String
description: Problem Description and Solution for Maximize Number of Subsequences in a String
sidebar_label: 2207. Maximize Number of Subsequences in a String
sidebar_position: 2207
---

# [2207. Maximize Number of Subsequences in a String](https://leetcode.com/problems/maximize-number-of-subsequences-in-a-string/)

```py title=maximize-number-of-subsequences-in-a-string.py
class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        p1, p2 = pattern
        
        if p1 == p2:
            n = text.count(p1) + 1
            
            return n * (n - 1) // 2
        
        def count(s):
            res = curr = 0
            
            for x in s:
                if x == p1:
                    curr += 1
                elif x == p2:
                    res += curr
            
            return res
        
        return max(count(p1 + text), count(text + p2))
```


