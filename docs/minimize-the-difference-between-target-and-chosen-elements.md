---
id: minimize-the-difference-between-target-and-chosen-elements
title: Minimize the Difference Between Target and Chosen Elements
description: Problem Description and Solution for Minimize the Difference Between Target and Chosen Elements
sidebar_label: 1981. Minimize the Difference Between Target and Chosen Elements
sidebar_position: 1981
---

# [1981. Minimize the Difference Between Target and Chosen Elements](https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/)

```py title=minimize-the-difference-between-target-and-chosen-elements.py
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        rows, cols = len(mat), len(mat[0])
        
        smallest = 0
        for row in mat:
            smallest += min(row)
        
        if smallest >= target: return smallest - target
        
        n = target * 2
        prev = [False] * n
        prev[0] = True
        
        for row in mat:
            row.sort()
            possible = [False] * n
            
            for i in range(n):
                if prev[i]:
                    for x in row:
                        if x + i >= n:
                            break
                        
                        possible[x + i] = True
            
            prev = possible
        
        res = target - smallest
        for i in range(n):
            if possible[i]:
                res = min(res, abs(i - target))
        
        return res
```


