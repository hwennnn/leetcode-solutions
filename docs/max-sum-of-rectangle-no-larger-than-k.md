---
id: max-sum-of-rectangle-no-larger-than-k
title: Max Sum of Rectangle No Larger Than K
description: Problem Description and Solution for Max Sum of Rectangle No Larger Than K
sidebar_label: 363. Max Sum of Rectangle No Larger Than K
sidebar_position: 363
---

# [363. Max Sum of Rectangle No Larger Than K](https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/)

```py title=max-sum-of-rectangle-no-larger-than-k.py
from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        maxSize = min(rows, cols)
        
        prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] += prefix[i + 1][j] + matrix[i][j]
        
        for i in range(rows):
            for j in range(cols):
                prefix[i + 1][j + 1] += prefix[i][j + 1]

        res = float('-inf')
        for row1 in range(rows):
            for row2 in range(row1, rows):
                sl = SortedList()
                sl.add(0)
                
                for j in range(cols):
                    curr = prefix[row2 + 1][j + 1] - prefix[row1][j + 1]
                    target = curr - k
                    
                    index = sl.bisect_left(target)
                    
                    if 0 <= index < len(sl):
                        res = max(res, curr - sl[index])
                    
                    sl.add(curr)

        return res
```


