---
id: can-place-flowers
title: Can Place Flowers
description: Problem Description and Solution for Can Place Flowers
sidebar_label: 605. Can Place Flowers
sidebar_position: 605
---

# [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

```py title=can-place-flowers.py
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], k: int) -> bool:
        n = len(flowerbed)
        put = i = 0
        
        while i < n:
            if flowerbed[i] == 1:
                i += 2
            else:
                if i == n - 1 or (i + 1 < n and flowerbed[i + 1] == 0):
                    put += 1
                    i += 2
                else:
                    i += 1
        
        return put >= k
```


