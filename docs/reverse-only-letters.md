---
id: reverse-only-letters
title: Reverse Only Letters
description: Problem Description and Solution for Reverse Only Letters
sidebar_label: 917. Reverse Only Letters
sidebar_position: 917
---

# [917. Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)

```py title=reverse-only-letters.py
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        
        i, j = 0, len(s) - 1
        
        while i < j:
            if not s[i].isalpha():
                i += 1
            elif not s[j].isalpha():
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        return "".join(s)
```


