---
id: positions-of-large-groups
title: Positions of Large Groups
description: Problem Description and Solution for Positions of Large Groups
sidebar_label: 830. Positions of Large Groups
sidebar_position: 830
---

# [830. Positions of Large Groups](https://leetcode.com/problems/positions-of-large-groups/)

```py title=positions-of-large-groups.py
class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        
        i, j, N, res = 0, 0, len(S), []
        
        while i < N:
            while j < N and S[i] == S[j]:
                j += 1
                
            if j-i >= 3:
                res.append([i, j-1])
            
            i = j
        
        return res
                
```


