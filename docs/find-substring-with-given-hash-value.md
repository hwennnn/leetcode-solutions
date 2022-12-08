---
id: find-substring-with-given-hash-value
title: Find Substring With Given Hash Value
description: Problem Description and Solution for Find Substring With Given Hash Value
sidebar_label: 2156. Find Substring With Given Hash Value
sidebar_position: 2156
---

# [2156. Find Substring With Given Hash Value](https://leetcode.com/problems/find-substring-with-given-hash-value/)

```py title=find-substring-with-given-hash-value.py
class Solution:
    def subStrHash(self, s: str, power: int, M: int, k: int, hashValue: int) -> str:
        def val(x):
            return ord(x) - ord('a') + 1
        
        curr = 0
        b = 1
        res = n = len(s)
        
        for i in range(n - 1, -1, -1):
            curr = (curr * power + val(s[i])) % M
            
            if i + k >= n:
                b = b * power % M
            else:
                curr = (curr - val(s[i + k]) * b) % M
            
            if curr == hashValue:
                res = i
        
        return s[res: res + k]
```


