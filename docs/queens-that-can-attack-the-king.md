---
id: queens-that-can-attack-the-king
title: Queens That Can Attack the King
description: Problem Description and Solution for Queens That Can Attack the King
sidebar_label: 1222. Queens That Can Attack the King
sidebar_position: 1222
---

# [1222. Queens That Can Attack the King](https://leetcode.com/problems/queens-that-can-attack-the-king/)

```py title=queens-that-can-attack-the-king.py
class Solution:
    def queensAttacktheKing(self, queens, king):
        res = []
        queens = {(i, j) for i, j in queens}
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                for k in range(1, 8):
                    x, y = king[0] + i * k, king[1] + j * k
                    if (x, y) in queens:
                        res.append([x, y])
                        break
        return res
```


