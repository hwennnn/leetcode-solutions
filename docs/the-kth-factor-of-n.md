---
id: the-kth-factor-of-n
title: The kth Factor of n
description: Problem Description and Solution for The kth Factor of n
sidebar_label: 1492. The kth Factor of n
sidebar_position: 1492
---

# [1492. The kth Factor of n](https://leetcode.com/problems/the-kth-factor-of-n/)

```py title=the-kth-factor-of-n.py
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = set()
        
        for i in range(1, n+1):
            if n % i == 0:
                res.add(i)
                res.add(n//i)
                
        res = sorted(list(res))

        return res[k-1] if len(res) >= k else -1
```


