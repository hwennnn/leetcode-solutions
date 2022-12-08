---
id: find-the-town-judge
title: Find the Town Judge
description: Problem Description and Solution for Find the Town Judge
sidebar_label: 997. Find the Town Judge
sidebar_position: 997
---

# [997. Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

```py title=find-the-town-judge.py
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        trust_other = [0] * (n + 1)
        
        for u, v in trust:
            trusted[v] += 1
            trust_other[u] += 1
        
        for i in range(1, n + 1):
            if trusted[i] == n - 1 and trust_other[i] == 0:
                return i
        
        return -1
```


