---
id: palindrome-number
title: Palindrome Number
description: Problem Description and Solution for Palindrome Number
sidebar_label: 9. Palindrome Number
sidebar_position: 9
---

# [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)

```py title=palindrome-number.py
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        i, j = 0, len(x)-1
        
        while i < j and x[i] == x[j]:
            i += 1
            j -= 1
        
        return i >= j
```


