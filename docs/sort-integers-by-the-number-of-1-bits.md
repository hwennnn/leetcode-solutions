---
id: sort-integers-by-the-number-of-1-bits
title: Sort Integers by The Number of 1 Bits
description: Problem Description and Solution for Sort Integers by The Number of 1 Bits
sidebar_label: 1356. Sort Integers by The Number of 1 Bits
sidebar_position: 1356
---

# [1356. Sort Integers by The Number of 1 Bits](https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/)

```py title=sort-integers-by-the-number-of-1-bits.py
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x : (x.bit_count(), x))
        return arr
```


