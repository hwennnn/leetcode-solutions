---
id: remove-colored-pieces-if-both-neighbors-are-the-same-color
title: Remove Colored Pieces if Both Neighbors are the Same Color
description: Problem Description and Solution for Remove Colored Pieces if Both Neighbors are the Same Color
sidebar_label: 2038. Remove Colored Pieces if Both Neighbors are the Same Color
sidebar_position: 2038
---

# [2038. Remove Colored Pieces if Both Neighbors are the Same Color](https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/)

```py title=remove-colored-pieces-if-both-neighbors-are-the-same-color.py
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        a = b = 0
        
        for i in range(1, n - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == 'A':
                    a += 1
                else:
                    b += 1
        
        return a > b
```


