---
id: richest-customer-wealth
title: Richest Customer Wealth
description: Problem Description and Solution for Richest Customer Wealth
sidebar_label: 1672. Richest Customer Wealth
sidebar_position: 1672
---

# [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/)

```py title=richest-customer-wealth.py
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(A) for A in accounts)
```


