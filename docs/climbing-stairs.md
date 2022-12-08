---
id: climbing-stairs
title: Climbing Stairs
description: Problem Description and Solution for Climbing Stairs
sidebar_label: 70. Climbing Stairs
sidebar_position: 70
---

# [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)

```py title=climbing-stairs.py
class Solution:
    def climbStairs(self, n: int) -> int:
        prev, curr = 1, 1
        
        for _ in range(n - 1):
            curr, prev = curr + prev, curr
        
        return curr
```


