---
id: combination-sum-iii
title: Combination Sum III
description: Problem Description and Solution for Combination Sum III
sidebar_label: 216. Combination Sum III
sidebar_position: 216
---

# [216. Combination Sum III](https://leetcode.com/problems/combination-sum-iii/)

```py title=combination-sum-iii.py
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def go(x, curr):
            if x == 10 or len(curr) == k:
                if len(curr) == k and sum(curr) == n:
                    res.append(curr)
                return
            
            go(x + 1, curr)
            go(x + 1, curr + [x])

        go(1, [])
        
        return res
```


