---
id: minimum-money-required-before-transactions
title: Minimum Money Required Before Transactions
description: Problem Description and Solution for Minimum Money Required Before Transactions
sidebar_label: 2412. Minimum Money Required Before Transactions
sidebar_position: 2412
---

# [2412. Minimum Money Required Before Transactions](https://leetcode.com/problems/minimum-money-required-before-transactions/)

```py title=minimum-money-required-before-transactions.py
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        diff = sum(max(0, i - j) for i, j in transactions)
        res = 0
        
        for i, j in transactions:
            res = max(res, diff - max(0, i - j) + i)
        
        return res
```


