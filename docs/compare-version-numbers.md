---
id: compare-version-numbers
title: Compare Version Numbers
description: Problem Description and Solution for Compare Version Numbers
sidebar_label: 165. Compare Version Numbers
sidebar_position: 165
---

# [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)

```py title=compare-version-numbers.py
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        A = map(int, version1.split('.'))
        B = map(int, version2.split('.'))
        
        for v1, v2 in zip_longest(A, B, fillvalue=0):
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
                
            
        return 0
            
```


