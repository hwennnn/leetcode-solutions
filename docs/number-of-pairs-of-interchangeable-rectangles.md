---
id: number-of-pairs-of-interchangeable-rectangles
title: Number of Pairs of Interchangeable Rectangles
description: Problem Description and Solution for Number of Pairs of Interchangeable Rectangles
sidebar_label: 2001. Number of Pairs of Interchangeable Rectangles
sidebar_position: 2001
---

# [2001. Number of Pairs of Interchangeable Rectangles](https://leetcode.com/problems/number-of-pairs-of-interchangeable-rectangles/)

```py title=number-of-pairs-of-interchangeable-rectangles.py
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        mp = collections.Counter()
        res = 0
        
        for x,y in rectangles:
            f = gcd(x, y)
            x //= f
            y //= f
            
            res += mp[(x, y)]
            mp[(x, y)] += 1
        
        return res
        
```


