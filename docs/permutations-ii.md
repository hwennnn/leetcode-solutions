---
id: permutations-ii
title: Permutations II
description: Problem Description and Solution for Permutations II
sidebar_label: 47. Permutations II
sidebar_position: 47
---

# [47. Permutations II](https://leetcode.com/problems/permutations-ii/)

```py title=permutations-ii.py
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        
        def backtrack(mask, path):
            if len(path) == n:
                res.append(path)
                return
            
            for i in range(n):
                if mask & (1 << i) > 0: continue
                
                if i > 0 and nums[i] == nums[i - 1] and mask & (1 << (i - 1)) > 0: continue
                
                backtrack(mask | (1 << i), path + [nums[i]])
        
        backtrack(0, [])
        return res
```


