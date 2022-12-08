---
id: check-if-every-row-and-column-contains-all-numbers
title: Check if Every Row and Column Contains All Numbers
description: Problem Description and Solution for Check if Every Row and Column Contains All Numbers
sidebar_label: 2133. Check if Every Row and Column Contains All Numbers
sidebar_position: 2133
---

# [2133. Check if Every Row and Column Contains All Numbers](https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/)

```py title=check-if-every-row-and-column-contains-all-numbers.py
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for row in matrix:
            if len(set(row)) != n: return False
        
        for col in zip(*matrix):
            if len(set(col)) != n: return False
        
        return True
```


