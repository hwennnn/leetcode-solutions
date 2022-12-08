---
id: check-if-all-as-appears-before-all-bs
title: Check if All A's Appears Before All B's
description: Problem Description and Solution for Check if All A's Appears Before All B's
sidebar_label: 2124. Check if All A's Appears Before All B's
sidebar_position: 2124
---

# [2124. Check if All A's Appears Before All B's](https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/)

```py title=check-if-all-as-appears-before-all-bs.py
class Solution:
    def checkString(self, s: str) -> bool:
        aCount = 0
        a = s.count("a")
        
        for c in s:
            if c == "a":
                aCount += 1
            elif c == "b":
                if aCount != a:
                    return False
        
        return True
```


