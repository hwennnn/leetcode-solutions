---
id: powerful-integers
title: Powerful Integers
description: Problem Description and Solution for Powerful Integers
sidebar_label: 970. Powerful Integers
sidebar_position: 970
---

# [970. Powerful Integers](https://leetcode.com/problems/powerful-integers/)

```py title=powerful-integers.py
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        
        for i in range(100):
            for j in range(100):
                z = x ** i + y ** j
                if z <= bound:
                    res.add(z)
        
        return list(res)
```


