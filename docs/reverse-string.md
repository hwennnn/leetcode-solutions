---
id: reverse-string
title: Reverse String
description: Problem Description and Solution for Reverse String
sidebar_label: 344. Reverse String
sidebar_position: 344
---

# [344. Reverse String](https://leetcode.com/problems/reverse-string/)

```py title=reverse-string.py
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i, j = 0, n - 1
        
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

```


