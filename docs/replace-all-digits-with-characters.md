---
id: replace-all-digits-with-characters
title: Replace All Digits with Characters
description: Problem Description and Solution for Replace All Digits with Characters
sidebar_label: 1844. Replace All Digits with Characters
sidebar_position: 1844
---

# [1844. Replace All Digits with Characters](https://leetcode.com/problems/replace-all-digits-with-characters/)

```py title=replace-all-digits-with-characters.py
class Solution:
    def replaceDigits(self, s: str) -> str:
        res = []
        
        for i, c in enumerate(s):
            if c.isnumeric():
                res.append(chr(ord(s[i-1]) + int(c)))
            else:
                res.append(c)
        
        return "".join(res)
```


