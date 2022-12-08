---
id: number-of-good-ways-to-split-a-string
title: Number of Good Ways to Split a String
description: Problem Description and Solution for Number of Good Ways to Split a String
sidebar_label: 1525. Number of Good Ways to Split a String
sidebar_position: 1525
---

# [1525. Number of Good Ways to Split a String](https://leetcode.com/problems/number-of-good-ways-to-split-a-string/)

```py title=number-of-good-ways-to-split-a-string.py
class Solution:
    def numSplits(self, S: str) -> int:
        n = len(S)
        prefix = [None] * n
        suffix = [None] * n
        mp = set()
        res = 0
        
        for i in range(n):
            mp.add(S[i])
            prefix[i] = len(mp)
            
        mp.clear()
        
        for i in reversed(range(n)):
            mp.add(S[i])
            suffix[i] = len(mp)
        

        for i in range(1,n):
            res += prefix[i-1] == suffix[i]
        
        return res
```


