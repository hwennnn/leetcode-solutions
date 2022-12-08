---
id: minimum-cost-to-cut-a-stick
title: Minimum Cost to Cut a Stick
description: Problem Description and Solution for Minimum Cost to Cut a Stick
sidebar_label: 1547. Minimum Cost to Cut a Stick
sidebar_position: 1547
---

# [1547. Minimum Cost to Cut a Stick](https://leetcode.com/problems/minimum-cost-to-cut-a-stick/)

```py title=minimum-cost-to-cut-a-stick.py
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts = [0] + cuts + [n]
        cuts.sort()
        
        @cache
        def go(i, j):
            if j - i <= 1: return 0
            
            res = float('inf')
            
            for k in range(i + 1, j):
                res = min(res, go(i, k) + go(k, j) + cuts[j] - cuts[i])
            
            return res
        
        return go(0, len(cuts) - 1)
```


