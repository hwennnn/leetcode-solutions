---
id: find-a-peak-element-ii
title: Find a Peak Element II
description: Problem Description and Solution for Find a Peak Element II
sidebar_label: 1901. Find a Peak Element II
sidebar_position: 1901
---

# [1901. Find a Peak Element II](https://leetcode.com/problems/find-a-peak-element-ii/)

```py title=find-a-peak-element-ii.py
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        
        top = 0
        bottom = rows - 1
        
        while bottom > top:
            mid = (top + bottom) // 2
            if max(mat[mid]) > max(mat[mid+1]):
                bottom = mid
            else:
                top = mid + 1
                
        return [bottom, mat[bottom].index(max(mat[bottom]))]
```


