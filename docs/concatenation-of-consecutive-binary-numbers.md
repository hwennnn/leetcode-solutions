---
id: concatenation-of-consecutive-binary-numbers
title: Concatenation of Consecutive Binary Numbers
description: Problem Description and Solution for Concatenation of Consecutive Binary Numbers
sidebar_label: 1680. Concatenation of Consecutive Binary Numbers
sidebar_position: 1680
---

# [1680. Concatenation of Consecutive Binary Numbers](https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/)

```py title=concatenation-of-consecutive-binary-numbers.py
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        M = 10 ** 9 + 7
        
        total = 0
        for x in range(1, n + 1):
            total *= pow(2, x.bit_length())
            total += x
            total %= M
        
        return total
```


