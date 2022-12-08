---
id: mirror-reflection
title: Mirror Reflection
description: Problem Description and Solution for Mirror Reflection
sidebar_label: 858. Mirror Reflection
sidebar_position: 858
---

# [858. Mirror Reflection](https://leetcode.com/problems/mirror-reflection/)

```py title=mirror-reflection.py
class Solution:
    def mirrorReflection(self, p, q):
        while p % 2 == 0 and q % 2 == 0: p, q = p // 2, q // 2
        return 1 - p % 2 + q % 2
```


