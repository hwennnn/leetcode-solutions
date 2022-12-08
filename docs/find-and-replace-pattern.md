---
id: find-and-replace-pattern
title: Find and Replace Pattern
description: Problem Description and Solution for Find and Replace Pattern
sidebar_label: 890. Find and Replace Pattern
sidebar_position: 890
---

# [890. Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)

```py title=find-and-replace-pattern.py
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def h(word):
            s = {}
            res = []
            
            for x in word:
                if x not in s:
                    s[x] = len(s)
                    
                res.append(s[x])
            
            return "".join(map(str, res))
        
        target = h(pattern)
        res = []
        
        for word in words:
            if h(word) == target:
                res.append(word)
        
        return res
```


