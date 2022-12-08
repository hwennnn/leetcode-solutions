---
id: number-of-burgers-with-no-waste-of-ingredients
title: Number of Burgers with No Waste of Ingredients
description: Problem Description and Solution for Number of Burgers with No Waste of Ingredients
sidebar_label: 1276. Number of Burgers with No Waste of Ingredients
sidebar_position: 1276
---

# [1276. Number of Burgers with No Waste of Ingredients](https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/)

```py title=number-of-burgers-with-no-waste-of-ingredients.py
class Solution:
    def numOfBurgers(self, t: int, c: int) -> List[int]:
        return [(t//2) - c, c * 2 - t // 2] if t % 2 == 0 and c*2 <= t <= c*4 else []
```


