---
id: camelcase-matching
title: Camelcase Matching
description: Problem Description and Solution for Camelcase Matching
sidebar_label: 1023. Camelcase Matching
sidebar_position: 1023
---

# [1023. Camelcase Matching](https://leetcode.com/problems/camelcase-matching/)

```py title=camelcase-matching.py
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        m, n = len(queries), len(pattern)
        res = [False] * m
        
        for i, words in enumerate(queries):
            index = 0
            valid = True
            
            for word in words:
                if ord("A") <= ord(word) <= ord("Z") and (index == n or word != pattern[index]):
                    valid = False
                    break
                    
                if index < n and word == pattern[index]:
                    index += 1
            
            res[i] = valid and index == n
        
        return res
```


