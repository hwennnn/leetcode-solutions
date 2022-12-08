---
id: happy-number
title: Happy Number
description: Problem Description and Solution for Happy Number
sidebar_label: 202. Happy Number
sidebar_position: 202
---

# [202. Happy Number](https://leetcode.com/problems/happy-number/)

```py title=happy-number.py
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            curr = 0
            
            while n > 0:
                a, b = divmod(n, 10)
                curr += b * b
                n = a
            
            n = curr
        
        return n == 1
```


