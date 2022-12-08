---
id: find-numbers-with-even-number-of-digits
title: Find Numbers with Even Number of Digits
description: Problem Description and Solution for Find Numbers with Even Number of Digits
sidebar_label: 1295. Find Numbers with Even Number of Digits
sidebar_position: 1295
---

# [1295. Find Numbers with Even Number of Digits](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/)

```py title=find-numbers-with-even-number-of-digits.py
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        
        for num in map(str,nums):
            res += (len(num) % 2 == 0)
        
        return res
```


