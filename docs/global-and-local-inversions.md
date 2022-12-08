---
id: global-and-local-inversions
title: Global and Local Inversions
description: Problem Description and Solution for Global and Local Inversions
sidebar_label: 775. Global and Local Inversions
sidebar_position: 775
---

# [775. Global and Local Inversions](https://leetcode.com/problems/global-and-local-inversions/)

```py title=global-and-local-inversions.py
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        return all(abs(i - v) <= 1 for i, v in enumerate(A))

```


