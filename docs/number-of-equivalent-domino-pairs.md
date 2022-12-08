---
id: number-of-equivalent-domino-pairs
title: Number of Equivalent Domino Pairs
description: Problem Description and Solution for Number of Equivalent Domino Pairs
sidebar_label: 1128. Number of Equivalent Domino Pairs
sidebar_position: 1128
---

# [1128. Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/)

```py title=number-of-equivalent-domino-pairs.py
class Solution:
    def numEquivDominoPairs(self, A: List[List[int]]) -> int:
        n = len(A)
        mp = collections.defaultdict(int)
        
        def make(A):
            return (min(A), max(A))
        
        res = 0
        for i in range(n):
            m = make(A[i])
            res += mp[m]
            
            mp[m] += 1
        
        return res
```


