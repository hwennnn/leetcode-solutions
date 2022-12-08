---
id: check-if-a-string-can-break-another-string
title: Check If a String Can Break Another String
description: Problem Description and Solution for Check If a String Can Break Another String
sidebar_label: 1433. Check If a String Can Break Another String
sidebar_position: 1433
---

# [1433. Check If a String Can Break Another String](https://leetcode.com/problems/check-if-a-string-can-break-another-string/)

```py title=check-if-a-string-can-break-another-string.py
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        
        def check(d1, d2):
            s = 0
            for c in "abcdefghijklmnopqrstuvwxyz":
                s += d1[c] - d2[c]
                if s < 0:
                    return False
            
            return True
        
        d1 = collections.Counter(s1)
        d2 = collections.Counter(s2)
        
        return check(d1,d2) or check(d2,d1)
```


