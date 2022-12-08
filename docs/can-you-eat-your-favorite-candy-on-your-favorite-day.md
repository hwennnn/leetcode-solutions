---
id: can-you-eat-your-favorite-candy-on-your-favorite-day
title: Can You Eat Your Favorite Candy on Your Favorite Day?
description: Problem Description and Solution for Can You Eat Your Favorite Candy on Your Favorite Day?
sidebar_label: 1744. Can You Eat Your Favorite Candy on Your Favorite Day?
sidebar_position: 1744
---

# [1744. Can You Eat Your Favorite Candy on Your Favorite Day?](https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/)

```py title=can-you-eat-your-favorite-candy-on-your-favorite-day.py
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        
        res = []
        prefix = [0] + list(accumulate(candiesCount))
            
        for favType, day, cap in queries:
            if (day+1) * cap > prefix[favType] and prefix[favType+1] >= (day+1) * 1:
                res.append(True)
            else:
                res.append(False)
            
        return res
```


