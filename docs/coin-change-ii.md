---
id: coin-change-ii
title: Coin Change II
description: Problem Description and Solution for Coin Change II
sidebar_label: 518. Coin Change II
sidebar_position: 518
---

# [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/)

```py title=coin-change-ii.py
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
                    
        return dp[amount]
```


