---
id: combinations
title: Combinations
description: Problem Description and Solution for Combinations
sidebar_label: 77. Combinations
sidebar_position: 77
---

# [77. Combinations](https://leetcode.com/problems/combinations/)

```py title=combinations.py
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        A = list(range(1, n + 1))
        res = []
        
        def backtrack(i, curr):
            if len(curr) == k:
                res.append(curr)
                return
            
            for j in range(i, len(A)):
                backtrack(j + 1, curr + [A[j]])
        
        backtrack(0, [])
        return res
```


