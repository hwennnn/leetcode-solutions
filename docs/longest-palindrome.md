---
id: longest-palindrome
title: Longest Palindrome
description: Problem Description and Solution for Longest Palindrome
sidebar_label: 409. Longest Palindrome
sidebar_position: 409
---

# [409. Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

```py title=longest-palindrome.py
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        
        for char in s:
            if char in odd:
                odd.remove(char)
            else:
                odd.add(char)
        
        return len(s) - len(odd) + int(len(odd) > 0)
        
```


