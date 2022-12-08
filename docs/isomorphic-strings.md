---
id: isomorphic-strings
title: Isomorphic Strings
description: Problem Description and Solution for Isomorphic Strings
sidebar_label: 205. Isomorphic Strings
sidebar_position: 205
---

# [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

```py title=isomorphic-strings.py
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        def construct(s):
            s = list(s)
            mp = {}
            res = ""
            
            for i, x in enumerate(s):
                if x not in mp:
                    mp[x] = len(mp)
                s[i] = mp[x]
                
            return s
        
        return construct(s) == construct(t)
            
```


