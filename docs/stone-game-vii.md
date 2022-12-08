---
id: stone-game-vii
title: Stone Game VII
description: Problem Description and Solution for Stone Game VII
sidebar_label: 1690. Stone Game VII
sidebar_position: 1690
---

# [1690. Stone Game VII](https://leetcode.com/problems/stone-game-vii/)

```py title=stone-game-vii.py
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        prefix = [0] + list(accumulate(stones))
        
        def dfs(i, j):
            if i == j: return 0
            if dp[i][j]: return dp[i][j]
            
            ssum = prefix[j + 1] - prefix[i]
            dp[i][j] = max(ssum - stones[i] - dfs(i + 1, j), ssum - stones[j] - dfs(i, j - 1))
            
            return dp[i][j]
        
        return dfs(0, n - 1)
```


