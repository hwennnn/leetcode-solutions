---
id: count-odd-numbers-in-an-interval-range
title: Count Odd Numbers in an Interval Range
description: Problem Description and Solution for Count Odd Numbers in an Interval Range
sidebar_label: 1523. Count Odd Numbers in an Interval Range
sidebar_position: 1523
---

# [1523. Count Odd Numbers in an Interval Range](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/)

```py title=count-odd-numbers-in-an-interval-range.py
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = 0
        
        if low & 1 or high & 1:
            res += 1
        
        return res + (high - low) // 2
```


