---
id: naming-a-company
title: Naming a Company
description: Problem Description and Solution for Naming a Company
sidebar_label: 2306. Naming a Company
sidebar_position: 2306
---

# [2306. Naming a Company](https://leetcode.com/problems/naming-a-company/)

```py title=naming-a-company.py
class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n = len(ideas)
        counts = [[0] * 26 for _ in range(26)]
        seen = set(ideas)
        orda = ord("a")
        
        for idea in ideas:
            for c in range(26):
                if chr(orda + c) + idea[1:] not in seen:
                    counts[ord(idea[0]) - orda][c] += 1
        
        res = 0
        
        for idea in ideas:
            for c in range(26):
                if chr(orda + c) + idea[1:] not in seen:
                    res += counts[c][ord(idea[0]) - orda]
        
        return res
                
        
```


