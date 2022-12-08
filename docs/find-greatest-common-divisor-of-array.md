---
id: find-greatest-common-divisor-of-array
title: Find Greatest Common Divisor of Array
description: Problem Description and Solution for Find Greatest Common Divisor of Array
sidebar_label: 1979. Find Greatest Common Divisor of Array
sidebar_position: 1979
---

# [1979. Find Greatest Common Divisor of Array](https://leetcode.com/problems/find-greatest-common-divisor-of-array/)

```py title=find-greatest-common-divisor-of-array.py
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(max(nums), min(nums))
```


