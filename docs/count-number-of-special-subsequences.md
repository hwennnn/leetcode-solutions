---
id: count-number-of-special-subsequences
title: Count Number of Special Subsequences
description: Problem Description and Solution for Count Number of Special Subsequences
sidebar_label: 1955. Count Number of Special Subsequences
sidebar_position: 1955
---

# [1955. Count Number of Special Subsequences](https://leetcode.com/problems/count-number-of-special-subsequences/)

```py title=count-number-of-special-subsequences.py
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        a = b = c = 0
        M = 10 ** 9 + 7
        
        for x in nums:
            if x == 0:
                a += a + 1
            elif x == 1:
                b += b + a
            else:
                c += c + b
                c %= M
        
        return c
```


