---
id: break-a-palindrome
title: Break a Palindrome
description: Problem Description and Solution for Break a Palindrome
sidebar_label: 1328. Break a Palindrome
sidebar_position: 1328
---

# [1328. Break a Palindrome](https://leetcode.com/problems/break-a-palindrome/)

```py title=break-a-palindrome.py
class Solution:
    def breakPalindrome(self, A: str) -> str:
        if len(A) < 2: return ''
        
        for i in range(len(A) // 2):
            if A[i] != 'a':
                return A[:i] + 'a' + A[i + 1:]
        
        return A[:-1] + 'b'
```


