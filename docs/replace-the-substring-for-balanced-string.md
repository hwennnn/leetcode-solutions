---
id: replace-the-substring-for-balanced-string
title: Replace the Substring for Balanced String
description: Problem Description and Solution for Replace the Substring for Balanced String
sidebar_label: 1234. Replace the Substring for Balanced String
sidebar_position: 1234
---

# [1234. Replace the Substring for Balanced String](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)

```py title=replace-the-substring-for-balanced-string.py
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        desired = n // 4
        c = Counter(s)
        
        for key in c:
            if c[key] > 0:
                c[key] = max(0, c[key] - desired)
        
        res = n
        i = 0
        
        for j,x in enumerate(s):
            c[x] -= 1
            
            while i < n and all(val <= 0 for val in c.values()):
                res = min(res, j - i + 1)
                c[s[i]] += 1
                i += 1
        
        return res
```


