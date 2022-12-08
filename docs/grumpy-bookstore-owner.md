---
id: grumpy-bookstore-owner
title: Grumpy Bookstore Owner
description: Problem Description and Solution for Grumpy Bookstore Owner
sidebar_label: 1052. Grumpy Bookstore Owner
sidebar_position: 1052
---

# [1052. Grumpy Bookstore Owner](https://leetcode.com/problems/grumpy-bookstore-owner/)

```py title=grumpy-bookstore-owner.py
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        A = [i for i in range(n) if grumpy[i] == 1]

        res = customers[A[0]] if A else 0
        if A:
            curr, start = customers[A[0]], 0
            for index in A[1:]:
                if index - A[start] < minutes:
                    curr += customers[index]
                else:
                    while index - A[start] >= minutes:
                        curr -= customers[A[start]]
                        start += 1
                    curr += customers[index]

                res = max(res, curr)
        
        return res + sum(customers[i] for i in range(n) if grumpy[i] == 0)
```


