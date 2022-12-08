---
id: palindromic-substrings
title: Palindromic Substrings
description: Problem Description and Solution for Palindromic Substrings
sidebar_label: 647. Palindromic Substrings
sidebar_position: 647
---

# [647. Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/)

```py title=palindromic-substrings.py
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        
        def helper(left, right):
            count = 0
            
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                count += 1
            
            return count
        
        for mid in range(n):
            res += helper(mid, mid)
            res += helper(mid, mid + 1)
        
        return res
```


