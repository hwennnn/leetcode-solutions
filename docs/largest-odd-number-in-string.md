---
id: largest-odd-number-in-string
title: Largest Odd Number in String
description: Problem Description and Solution for Largest Odd Number in String
sidebar_label: 1903. Largest Odd Number in String
sidebar_position: 1903
---

# [1903. Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string/)

```py title=largest-odd-number-in-string.py
class Solution:
    def largestOddNumber(self, nums: str) -> str:
        res = None
        
        for i,x in enumerate(nums):
            if int(x) & 1:
                res = nums[:i + 1]
        
        return "" if not res else res
```


