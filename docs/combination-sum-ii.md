---
id: combination-sum-ii
title: Combination Sum II
description: Problem Description and Solution for Combination Sum II
sidebar_label: 40. Combination Sum II
sidebar_position: 40
---

# [40. Combination Sum II](https://leetcode.com/problems/combination-sum-ii/)

```py title=combination-sum-ii.py
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        res = []
        candidates.sort()
        
        def dfs(target, index, path):
            if target < 0: return
            
            if target == 0:
                res.append(path)
                return
            
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]: continue
                dfs(target - candidates[i], i + 1, path + [candidates[i]])
        
        dfs(target, 0, [])
        
        return res
```


