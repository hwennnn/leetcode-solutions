---
id: smallest-range-i
title: Smallest Range I
description: Problem Description and Solution for Smallest Range I
sidebar_label: 908. Smallest Range I
sidebar_position: 908
---

# [908. Smallest Range I](https://leetcode.com/problems/smallest-range-i/)

```py title=smallest-range-i.py
class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max(0, max(A) - min(A) - 2*K)
```


