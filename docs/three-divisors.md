---
id: three-divisors
title: Three Divisors
description: Problem Description and Solution for Three Divisors
sidebar_label: 1952. Three Divisors
sidebar_position: 1952
---

# [1952. Three Divisors](https://leetcode.com/problems/three-divisors/)

```py title=three-divisors.py
class Solution:
    def isThree(self, n: int) -> bool:
        res = 0
        
        for k in range(1, n + 1):
            if n % k == 0: res += 1
            
            if res > 3: return False
        
        return res == 3
```


