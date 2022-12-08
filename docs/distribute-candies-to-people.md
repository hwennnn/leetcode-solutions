---
id: distribute-candies-to-people
title: Distribute Candies to People
description: Problem Description and Solution for Distribute Candies to People
sidebar_label: 1103. Distribute Candies to People
sidebar_position: 1103
---

# [1103. Distribute Candies to People](https://leetcode.com/problems/distribute-candies-to-people/)

```py title=distribute-candies-to-people.py
class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        t = i = 0
        res = [0] * n
        
        while candies > 0:
            t += 1
            give = min(t, candies)
            candies -= give
            res[i] += give
            
            i = (i + 1) % n
            
        return res
```


