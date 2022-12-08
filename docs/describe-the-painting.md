---
id: describe-the-painting
title: Describe the Painting
description: Problem Description and Solution for Describe the Painting
sidebar_label: 1943. Describe the Painting
sidebar_position: 1943
---

# [1943. Describe the Painting](https://leetcode.com/problems/describe-the-painting/)

```py title=describe-the-painting.py
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        painting = [0] * (10 ** 5 + 1)
        ends = set()
        
        for start, end, color in segments:
            painting[start] += color
            painting[end] -= color
            ends.add(end)
        
        for i in range(1, 10 ** 5 + 1):
            painting[i] += painting[i - 1]

        res = []
        currentStart = -1
        currentColor = 0
        
        for i, x in enumerate(painting):
            if i in ends or currentColor != x:
                if currentColor > 0:
                    res.append([currentStart, i, currentColor])
                currentStart = i
                currentColor = x

        return res
```


