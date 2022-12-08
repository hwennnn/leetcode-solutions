---
id: remove-digit-from-number-to-maximize-result
title: Remove Digit From Number to Maximize Result
description: Problem Description and Solution for Remove Digit From Number to Maximize Result
sidebar_label: 2259. Remove Digit From Number to Maximize Result
sidebar_position: 2259
---

# [2259. Remove Digit From Number to Maximize Result](https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/)

```py title=remove-digit-from-number-to-maximize-result.py
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        res = ""
        
        for i, x in enumerate(number):
            if x == digit:
                res = max(res, number[:i] + number[i + 1:])
        
        return res
```


