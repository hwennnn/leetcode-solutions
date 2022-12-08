---
id: stone-game-iv
title: Stone Game IV
description: Problem Description and Solution for Stone Game IV
sidebar_label: 1510. Stone Game IV
sidebar_position: 1510
---

# [1510. Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

```py title=stone-game-iv.py
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        dp = [False] * (n+1)
        
        for x in range(n+1):
            if not dp[x]:
                y = 1
                while x + y*y <= n:
                    dp[x+y*y] = True
                    y += 1
        
        return dp[n]
```


