---
id: number-of-rectangles-that-can-form-the-largest-square
title: Number Of Rectangles That Can Form The Largest Square
description: Problem Description and Solution for Number Of Rectangles That Can Form The Largest Square
sidebar_label: 1725. Number Of Rectangles That Can Form The Largest Square
sidebar_position: 1725
---

# [1725. Number Of Rectangles That Can Form The Largest Square](https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/)

```py title=number-of-rectangles-that-can-form-the-largest-square.py
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        res = []
        
        for a,b in rectangles:
            res.append(min(a,b))
        
        return res.count(max(res))
```


