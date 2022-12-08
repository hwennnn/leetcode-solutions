---
id: keep-multiplying-found-values-by-two
title: Keep Multiplying Found Values by Two
description: Problem Description and Solution for Keep Multiplying Found Values by Two
sidebar_label: 2154. Keep Multiplying Found Values by Two
sidebar_position: 2154
---

# [2154. Keep Multiplying Found Values by Two](https://leetcode.com/problems/keep-multiplying-found-values-by-two/)

```py title=keep-multiplying-found-values-by-two.py
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        s = set(nums)
        res = original
        found = res in s
        
        while found:
            res *= 2
            found = res in s
        
        return res
```


