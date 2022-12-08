---
id: permutation-in-string
title: Permutation in String
description: Problem Description and Solution for Permutation in String
sidebar_label: 567. Permutation in String
sidebar_position: 567
---

# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

```py title=permutation-in-string.py
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp = collections.Counter(s1)
        i = 0
        
        for j, x in enumerate(s2):
            mp[x] -= 1
            
            while mp[x] < 0:
                mp[s2[i]] += 1
                i += 1
            
            if j - i + 1 == len(s1):
                return True
        
        return False
```


