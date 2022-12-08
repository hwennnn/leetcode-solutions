---
id: number-of-ways-to-rearrange-sticks-with-k-sticks-visible
title: Number of Ways to Rearrange Sticks With K Sticks Visible
description: Problem Description and Solution for Number of Ways to Rearrange Sticks With K Sticks Visible
sidebar_label: 1866. Number of Ways to Rearrange Sticks With K Sticks Visible
sidebar_position: 1866
---

# [1866. Number of Ways to Rearrange Sticks With K Sticks Visible](https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/)

```py title=number-of-ways-to-rearrange-sticks-with-k-sticks-visible.py
class Solution:
    @cache
    def rearrangeSticks(self, n: int, k: int, M = 10 ** 9 + 7) -> int:
        if n == k: return 1
        if k == 0: return 0
        
        return (self.rearrangeSticks(n - 1, k - 1) + self.rearrangeSticks(n - 1, k) * (n - 1)) % M
```


