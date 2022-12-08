---
id: hamming-distance
title: Hamming Distance
description: Problem Description and Solution for Hamming Distance
sidebar_label: 461. Hamming Distance
sidebar_position: 461
---

# [461. Hamming Distance](https://leetcode.com/problems/hamming-distance/)

```py title=hamming-distance.py
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        res = 0
        
        while xor > 0:
            if xor & 1:
                res += 1
                
            xor >>= 1
            
        return res
```


