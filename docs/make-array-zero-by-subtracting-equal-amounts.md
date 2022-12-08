---
id: make-array-zero-by-subtracting-equal-amounts
title: Make Array Zero by Subtracting Equal Amounts
description: Problem Description and Solution for Make Array Zero by Subtracting Equal Amounts
sidebar_label: 2357. Make Array Zero by Subtracting Equal Amounts
sidebar_position: 2357
---

# [2357. Make Array Zero by Subtracting Equal Amounts](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/)

```py title=make-array-zero-by-subtracting-equal-amounts.py
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set([x for x in nums if x != 0]))
```


