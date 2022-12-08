---
id: determine-color-of-a-chessboard-square
title: Determine Color of a Chessboard Square
description: Problem Description and Solution for Determine Color of a Chessboard Square
sidebar_label: 1812. Determine Color of a Chessboard Square
sidebar_position: 1812
---

# [1812. Determine Color of a Chessboard Square](https://leetcode.com/problems/determine-color-of-a-chessboard-square/)

```py title=determine-color-of-a-chessboard-square.py
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        a, b = ord(coordinates[0]) - ord('a'), int(coordinates[1])
        
        return (a % 2 == 0 and b % 2 == 0) or (a & 1 and b & 1)
```


