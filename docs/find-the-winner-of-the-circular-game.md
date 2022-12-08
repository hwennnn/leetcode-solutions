---
id: find-the-winner-of-the-circular-game
title: Find the Winner of the Circular Game
description: Problem Description and Solution for Find the Winner of the Circular Game
sidebar_label: 1823. Find the Winner of the Circular Game
sidebar_position: 1823
---

# [1823. Find the Winner of the Circular Game](https://leetcode.com/problems/find-the-winner-of-the-circular-game/)

```py title=find-the-winner-of-the-circular-game.py
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        A = [i for i in range(1, n + 1)]
        
        i = (0 + k - 1) % len(A)
        
        while len(A) > 1:
            A.pop(i)   
            i = (((i + k) % len(A) ) - 1) % len(A)
        
        return A[0]
```


