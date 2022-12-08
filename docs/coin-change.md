---
id: coin-change
title: Coin Change
description: Problem Description and Solution for Coin Change
sidebar_label: 322. Coin Change
sidebar_position: 322
---

# [322. Coin Change](https://leetcode.com/problems/coin-change/)

```py title=coin-change.py
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for x in range(1, amount + 1):
            for coin in coins:
                if x >= coin:
                    dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return -1 if dp[amount] == float('inf') else dp[amount]
```


