---
id: longest-palindromic-substring
title: Longest Palindromic Substring
description: Problem Description and Solution for Longest Palindromic Substring
sidebar_label: 5. Longest Palindromic Substring
sidebar_position: 5
---

# [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

```py title=longest-palindromic-substring.py
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1: return s
        
        def pal(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                i -= 1
                j += 1
            
            i += 1
            j -= 1
            
            return s[i : j + 1]
        
        res = ''
        for i in range(n - 1):
            res = max(res, pal(i, i), pal(i, i + 1), key = len)
        
        return res
```


