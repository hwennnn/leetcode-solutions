---
id: minimum-amount-of-time-to-fill-cups
title: Minimum Amount of Time to Fill Cups
description: Problem Description and Solution for Minimum Amount of Time to Fill Cups
sidebar_label: 2335. Minimum Amount of Time to Fill Cups
sidebar_position: 2335
---

# [2335. Minimum Amount of Time to Fill Cups](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/)

```py title=minimum-amount-of-time-to-fill-cups.py
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)
```


