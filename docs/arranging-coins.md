---
id: arranging-coins
title: Arranging Coins
description: Problem Description and Solution for Arranging Coins
sidebar_label: 441. Arranging Coins
sidebar_position: 441
---

# [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/)

```py title=arranging-coins.py
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int) (sqrt(1 + (8 * n)) - 1) // 2
    
```


