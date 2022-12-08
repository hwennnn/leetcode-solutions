---
id: split-a-string-in-balanced-strings
title: Split a String in Balanced Strings
description: Problem Description and Solution for Split a String in Balanced Strings
sidebar_label: 1221. Split a String in Balanced Strings
sidebar_position: 1221
---

# [1221. Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/)

```py title=split-a-string-in-balanced-strings.py
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = res = 0
        
        for c in s:
            if c == "R": r += 1
            else: l += 1
            
            res += l == r
        
        return res
```


