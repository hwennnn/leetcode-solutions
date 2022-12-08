---
id: find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
title: Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
description: Problem Description and Solution for Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
sidebar_label: 1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
sidebar_position: 1414
---

# [1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/)

```py title=find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k.py
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        
        while fib[-1] < k:
            fib.append(fib[-1] + fib[-2])
        
        res = 0
        i = len(fib) - 1        
        
        while k > 0:
            res += k // fib[i]
            k %= fib[i]
            i -= 1
        
        return res
```


