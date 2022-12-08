---
id: number-of-ways-to-paint-n-3-grid
title: Number of Ways to Paint N × 3 Grid
description: Problem Description and Solution for Number of Ways to Paint N × 3 Grid
sidebar_label: 1411. Number of Ways to Paint N × 3 Grid
sidebar_position: 1411
---

# [1411. Number of Ways to Paint N × 3 Grid](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/)

```py title=number-of-ways-to-paint-n-3-grid.py
class Solution:
    def numOfWays(self, n: int) -> int:
        a121, a123, mod = 6, 6, 10**9 + 7
        for i in range(n - 1):
            a121, a123 = a121 * 3 + a123 * 2, a121 * 2 + a123 * 2
        return (a121 + a123) % mod

```


