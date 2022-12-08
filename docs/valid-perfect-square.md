---
id: valid-perfect-square
title: Valid Perfect Square
description: Problem Description and Solution for Valid Perfect Square
sidebar_label: 367. Valid Perfect Square
sidebar_position: 367
---

# [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

```py title=valid-perfect-square.py
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, 10 ** 18
        
        while left < right:
            mid = left + (right - left) // 2
            
            if mid * mid >= num:
                right = mid
            else:
                left = mid + 1
        
        return left * left == num
```


