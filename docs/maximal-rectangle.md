---
id: maximal-rectangle
title: Maximal Rectangle
description: Problem Description and Solution for Maximal Rectangle
sidebar_label: 85. Maximal Rectangle
sidebar_position: 85
---

# [85. Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/)

```py title=maximal-rectangle.py
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        
        rows, cols = len(matrix), len(matrix[0])
        left = [0] * cols
        right = [cols] * cols
        heights = [0] * cols
        res = 0
        
        for i in range(rows):
            currLeft, currRight = 0, cols
            
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0
            
            for j in range(cols):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], currLeft)
                else:
                    left[j] = 0
                    currLeft = j + 1
            
            for j in range(cols - 1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], currRight)
                else:
                    right[j] = cols
                    currRight = j
            
            for j in range(cols):
                res = max(res, (right[j] - left[j]) * heights[j])

        return res
```


