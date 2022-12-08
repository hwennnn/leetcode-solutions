---
id: reordered-power-of-2
title: Reordered Power of 2
description: Problem Description and Solution for Reordered Power of 2
sidebar_label: 869. Reordered Power of 2
sidebar_position: 869
---

# [869. Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/)

```py title=reordered-power-of-2.py
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        c = collections.Counter(str(N))
        
        return any([c == collections.Counter(str(1 << n)) for n in range(30)])
```


