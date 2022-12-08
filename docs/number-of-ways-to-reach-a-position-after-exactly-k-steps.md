---
id: number-of-ways-to-reach-a-position-after-exactly-k-steps
title: Number of Ways to Reach a Position After Exactly k Steps
description: Problem Description and Solution for Number of Ways to Reach a Position After Exactly k Steps
sidebar_label: 2400. Number of Ways to Reach a Position After Exactly k Steps
sidebar_position: 2400
---

# [2400. Number of Ways to Reach a Position After Exactly k Steps](https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/)

```py title=number-of-ways-to-reach-a-position-after-exactly-k-steps.py
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        M = 10 ** 9 + 7
        
        @cache
        def dfs(pos, steps):
            if steps == k:
                return 1 if pos == endPos else 0
            
            remainingSteps = k - steps
            
            if abs(pos - endPos) > remainingSteps:
                return 0
                
            return (dfs(pos + 1, steps + 1) + dfs(pos - 1, steps + 1)) % M
    
        return dfs(startPos, 0)
```


