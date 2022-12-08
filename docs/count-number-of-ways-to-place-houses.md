---
id: count-number-of-ways-to-place-houses
title: Count Number of Ways to Place Houses
description: Problem Description and Solution for Count Number of Ways to Place Houses
sidebar_label: 2320. Count Number of Ways to Place Houses
sidebar_position: 2320
---

# [2320. Count Number of Ways to Place Houses](https://leetcode.com/problems/count-number-of-ways-to-place-houses/)

```py title=count-number-of-ways-to-place-houses.py
class Solution:
    def countHousePlacements(self, n: int) -> int:
        houses = spaces = 1
        total = houses + spaces
        M = 10 ** 9 + 7
        
        for i in range(1, n):
            houses = spaces
            spaces = total
            total = (houses + spaces) % M
        
        return total * total % M
        
```


