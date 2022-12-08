---
id: flipping-an-image
title: Flipping an Image
description: Problem Description and Solution for Flipping an Image
sidebar_label: 832. Flipping an Image
sidebar_position: 832
---

# [832. Flipping an Image](https://leetcode.com/problems/flipping-an-image/)

```py title=flipping-an-image.py
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        n = len(A)
        res = []
        
        for i in range(n):
            tmp = []
            for j in reversed(A[i]):
                tmp.append(j ^ 1)
            
            res.append(tmp)
            
        return res
```


