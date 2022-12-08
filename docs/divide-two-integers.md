---
id: divide-two-integers
title: Divide Two Integers
description: Problem Description and Solution for Divide Two Integers
sidebar_label: 29. Divide Two Integers
sidebar_position: 29
---

# [29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)

```py title=divide-two-integers.py
class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)
```


