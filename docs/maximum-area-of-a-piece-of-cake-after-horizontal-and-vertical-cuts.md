---
id: maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts
title: Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
description: Problem Description and Solution for Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
sidebar_label: 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
sidebar_position: 1465
---

# [1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/)

```py title=maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts.py
class Solution:
    def maxArea(self, hn: int, wn: int, h: List[int], v: List[int]) -> int:
        h = [0] + sorted(h) + [hn]
        v = [0] + sorted(v) + [wn]            
        
        M = 10 ** 9 + 7
        h_diff = float('-inf')
        v_diff = float('-inf')
        
        for i in range(1, len(h)):
            h_diff = max(h_diff, h[i] - h[i - 1])
        
        for i in range(1, len(v)):
            v_diff = max(v_diff, v[i] - v[i - 1])
        
        return (h_diff * v_diff) % M
```


