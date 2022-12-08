---
id: largest-number
title: Largest Number
description: Problem Description and Solution for Largest Number
sidebar_label: 179. Largest Number
sidebar_position: 179
---

# [179. Largest Number](https://leetcode.com/problems/largest-number/)

```py title=largest-number.py
import functools 

class Solution:
    def largestNumber(self, nums):
        compare = lambda a, b: 1 if a+b > b+a else -1 if a+b < b+a else 0
        _nums = list(map(str, nums))
        _nums.sort(key=functools.cmp_to_key(compare), reverse=True)
        return str(int(''.join(_nums)))
```


