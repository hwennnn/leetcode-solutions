---
id: number-of-people-aware-of-a-secret
title: Number of People Aware of a Secret
description: Problem Description and Solution for Number of People Aware of a Secret
sidebar_label: 2327. Number of People Aware of a Secret
sidebar_position: 2327
---

# [2327. Number of People Aware of a Secret](https://leetcode.com/problems/number-of-people-aware-of-a-secret/)

```py title=number-of-people-aware-of-a-secret.py
class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        M = 10 ** 9 + 7
        res = 1
        
        canShare = defaultdict(int)
        canShare[delay] = 1
        
        toForget = defaultdict(int)
        toForget[forget] = 1

        propagate = 0
        
        for day in range(delay, n):
            propagate += canShare[day]    
            propagate -= toForget[day]
            
            res += propagate
            res -= toForget[day]
            res %= M
            
            canShare[day + delay] += propagate
            toForget[day + forget] += propagate
        
        return res % M
```


