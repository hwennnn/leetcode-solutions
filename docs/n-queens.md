---
id: n-queens
title: N-Queens
description: Problem Description and Solution for N-Queens
sidebar_label: 51. N-Queens
sidebar_position: 51
---

# [51. N-Queens](https://leetcode.com/problems/n-queens/)

```py title=n-queens.py
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols, diag1, diag2 = set(), set(), set()
        res = []
        
        def place(row, col):
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
        
        def discard(row, col):
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
        
        def ok(row, col):
            return col not in cols and (row - col) not in diag1 and (row + col) not in diag2
        
        def go(row):
            if row == n:
                nonlocal res
                
                res.append(["".join(b) for b in board])
                return
            
            for col in range(n):
                if ok(row, col):
                    place(row, col)
                    go(row + 1)
                    discard(row, col)
        
        go(0)
        
        return res
```


