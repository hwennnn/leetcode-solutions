---
id: binary-trees-with-factors
title: Binary Trees With Factors
description: Problem Description and Solution for Binary Trees With Factors
sidebar_label: 823. Binary Trees With Factors
sidebar_position: 823
---

# [823. Binary Trees With Factors](https://leetcode.com/problems/binary-trees-with-factors/)

```py title=binary-trees-with-factors.py
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        A = set(arr)
        M = 10 ** 9 + 7
        res = 0
        
        @cache
        def go(parent):
            cnt = 1
            
            for x in arr:
                if parent % x != 0: continue
                
                t = parent // x
                
                if t in A:
                    cnt += go(x) * go(t)
                    cnt %= M
            
            return cnt % M
        
        for x in arr:
            res += go(x)
            res %= M
        
        return res % M
```


