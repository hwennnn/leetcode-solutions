---
id: domino-and-tromino-tiling
title: Domino and Tromino Tiling
description: Problem Description and Solution for Domino and Tromino Tiling
sidebar_label: 790. Domino and Tromino Tiling
sidebar_position: 790
---

# [790. Domino and Tromino Tiling](https://leetcode.com/problems/domino-and-tromino-tiling/)

```py title=domino-and-tromino-tiling.py
class Solution:
    def numTilings(self, N):
        a, b, c = 0, 1, 1
        for i in range(N - 1): a, b, c = b, c, (c + c + a) % int(1e9 + 7)
        return c
```


