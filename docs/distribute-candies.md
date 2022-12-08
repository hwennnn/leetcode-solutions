---
id: distribute-candies
title: Distribute Candies
description: Problem Description and Solution for Distribute Candies
sidebar_label: 575. Distribute Candies
sidebar_position: 575
---

# [575. Distribute Candies](https://leetcode.com/problems/distribute-candies/)

```py title=distribute-candies.py
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        
        return int(min(len(candies)/2,len(set(candies))))
```


