---
id: find-first-palindromic-string-in-the-array
title: Find First Palindromic String in the Array
description: Problem Description and Solution for Find First Palindromic String in the Array
sidebar_label: 2108. Find First Palindromic String in the Array
sidebar_position: 2108
---

# [2108. Find First Palindromic String in the Array](https://leetcode.com/problems/find-first-palindromic-string-in-the-array/)

```py title=find-first-palindromic-string-in-the-array.py
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        res = ""
        
        for x in words:
            if x == x[::-1]:
                return x
        
        return res
```


