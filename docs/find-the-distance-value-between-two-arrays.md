---
id: find-the-distance-value-between-two-arrays
title: Find the Distance Value Between Two Arrays
description: Problem Description and Solution for Find the Distance Value Between Two Arrays
sidebar_label: 1385. Find the Distance Value Between Two Arrays
sidebar_position: 1385
---

# [1385. Find the Distance Value Between Two Arrays](https://leetcode.com/problems/find-the-distance-value-between-two-arrays/)

```py title=find-the-distance-value-between-two-arrays.py
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        for a1 in arr1:
            if all(abs(a1-a2) > d for a2 in arr2):
                count += 1

        return count
```


