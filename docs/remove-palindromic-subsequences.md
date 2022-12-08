---
id: remove-palindromic-subsequences
title: Remove Palindromic Subsequences
description: Problem Description and Solution for Remove Palindromic Subsequences
sidebar_label: 1332. Remove Palindromic Subsequences
sidebar_position: 1332
---

# [1332. Remove Palindromic Subsequences](https://leetcode.com/problems/remove-palindromic-subsequences/)

```py title=remove-palindromic-subsequences.py
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        return 2 - (s == s[::-1]) - (s == "")
```


