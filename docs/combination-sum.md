---
id: combination-sum
title: Combination Sum
description: Problem Description and Solution for Combination Sum
sidebar_label: 39. Combination Sum
sidebar_position: 39
---

# [39. Combination Sum](https://leetcode.com/problems/combination-sum/)

```py title=combination-sum.py
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        
        def go(index, curr, total):
            nonlocal res
            
            if total == target:
                res.append(curr)
                return
            
            if index == n:
                return
            
            for j in range(index, n):
                if total + candidates[j] <= target:
                    go(j, curr + [candidates[j]], total + candidates[j])
        
        go(0, [], 0)
        
        return res
```


