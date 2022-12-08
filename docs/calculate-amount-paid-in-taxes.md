---
id: calculate-amount-paid-in-taxes
title: Calculate Amount Paid in Taxes
description: Problem Description and Solution for Calculate Amount Paid in Taxes
sidebar_label: 2303. Calculate Amount Paid in Taxes
sidebar_position: 2303
---

# [2303. Calculate Amount Paid in Taxes](https://leetcode.com/problems/calculate-amount-paid-in-taxes/)

```py title=calculate-amount-paid-in-taxes.py
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        n = len(brackets)
        first = min(brackets[0][0], income)
        res =  first * (brackets[0][1] / 100)
        income -= first
        
        for i in range(1, n):
            k = brackets[i][0] - brackets[i - 1][0]
            curr = min(income, k)
            income -= curr
            res += curr * (brackets[i][1] / 100)
            
            if income == 0:
                break
        
        return res
```


