---
id: transpose-matrix
title: Transpose Matrix
description: Problem Description and Solution for Transpose Matrix
sidebar_label: 867. Transpose Matrix
sidebar_position: 867
---

# [867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)

```py title=transpose-matrix.py
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))
```


