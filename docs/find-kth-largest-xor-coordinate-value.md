---
id: find-kth-largest-xor-coordinate-value
title: Find Kth Largest XOR Coordinate Value
description: Problem Description and Solution for Find Kth Largest XOR Coordinate Value
sidebar_label: 1738. Find Kth Largest XOR Coordinate Value
sidebar_position: 1738
---

# [1738. Find Kth Largest XOR Coordinate Value](https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/)

```py title=find-kth-largest-xor-coordinate-value.py
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        
        for i in range(rows):
            for j in range(cols):
                if i:
                    matrix[i][j] ^= matrix[i-1][j]
                if j:
                    matrix[i][j] ^= matrix[i][j-1]
                if i and j:
                    matrix[i][j] ^= matrix[i-1][j-1]
                
                res.append(matrix[i][j])
                
        return sorted(res)[-k]
```


