---
id: fibonacci-number
title: Fibonacci Number
description: Problem Description and Solution for Fibonacci Number
sidebar_label: 509. Fibonacci Number
sidebar_position: 509
---

# [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)

```py title=fibonacci-number.py
class Solution:
    @cache
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        
        return self.fib(n - 1) + self.fib(n - 2)
```


