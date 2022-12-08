---
id: rank-transform-of-an-array
title: Rank Transform of an Array
description: Problem Description and Solution for Rank Transform of an Array
sidebar_label: 1331. Rank Transform of an Array
sidebar_position: 1331
---

# [1331. Rank Transform of an Array](https://leetcode.com/problems/rank-transform-of-an-array/)

```py title=rank-transform-of-an-array.py
class Solution:
    def arrayRankTransform(self, A: List[int]) -> List[int]:
        rank = {}
        for a in sorted(A):
            rank.setdefault(a, len(rank) + 1)
        return map(rank.get, A)
```


