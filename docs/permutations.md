---
id: permutations
title: Permutations
description: Problem Description and Solution for Permutations
sidebar_label: 46. Permutations
sidebar_position: 46
---

# [46. Permutations](https://leetcode.com/problems/permutations/)

```py title=permutations.py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        def go(curr, seen):
            nonlocal res
            
            if len(curr) == n:
                res.append(curr[:])
                return
            
            for i, x in enumerate(nums):
                if i in seen: continue
                seen.add(i)
                curr.append(x)
                go(curr, seen)
                seen.remove(i)
                curr.pop()
        
        go([], set())
        return res
```


