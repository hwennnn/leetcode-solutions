---
id: find-three-consecutive-integers-that-sum-to-a-given-number
title: Find Three Consecutive Integers That Sum to a Given Number
description: Problem Description and Solution for Find Three Consecutive Integers That Sum to a Given Number
sidebar_label: 2177. Find Three Consecutive Integers That Sum to a Given Number
sidebar_position: 2177
---

# [2177. Find Three Consecutive Integers That Sum to a Given Number](https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/)

```py title=find-three-consecutive-integers-that-sum-to-a-given-number.py
class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0: return []
        mid = num // 3
        return [mid - 1, mid, mid + 1]
```


