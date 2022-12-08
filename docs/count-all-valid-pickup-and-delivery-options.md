---
id: count-all-valid-pickup-and-delivery-options
title: Count All Valid Pickup and Delivery Options
description: Problem Description and Solution for Count All Valid Pickup and Delivery Options
sidebar_label: 1359. Count All Valid Pickup and Delivery Options
sidebar_position: 1359
---

# [1359. Count All Valid Pickup and Delivery Options](https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/)

```py title=count-all-valid-pickup-and-delivery-options.py
class Solution:
    def countOrders(self, n: int) -> int:
        M = 10 ** 9 + 7
        res = 1
        
        for i in range(2, n + 1):
            res *= i * (i * 2 - 1)
            res %= M
        
        return res
        
```


