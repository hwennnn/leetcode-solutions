---
id: sell-diminishing-valued-colored-balls
title: Sell Diminishing-Valued Colored Balls
description: Problem Description and Solution for Sell Diminishing-Valued Colored Balls
sidebar_label: 1648. Sell Diminishing-Valued Colored Balls
sidebar_position: 1648
---

# [1648. Sell Diminishing-Valued Colored Balls](https://leetcode.com/problems/sell-diminishing-valued-colored-balls/)

```py title=sell-diminishing-valued-colored-balls.py
from heapq import heappop, heappush

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        M = 10 ** 9 + 7
        
        pq = []
        for v in inventory:
            heappush(pq, (-v, 1))

        res = 0
        
        while pq and orders > 0:
            top, count = heappop(pq)
            top = -top
            
            while pq and top == -pq[0][0]:
                count += heappop(pq)[1]
            
            nextTop = 0
            if pq:
                nextTop = -pq[0][0]
                
            delta = top - nextTop
            
            if delta * count <= orders:
                d = (top*(top+1)) // 2
                d -= (nextTop*(nextTop+1)) // 2
                d *= count
                
                res += d
                res %= M
                orders -= (delta*count)
            
            else:
                cnt = orders // count
                d = (top*(top+1)) // 2
                nextTop = top - cnt
                d -= (nextTop*(nextTop+1)) // 2
                d *= count
                
                res += d
                res %= M
                orders -= (count * cnt)
                
                leftover = orders % count
                res += nextTop * leftover
                res %= M
                
                orders -= leftover
                
            if nextTop:
                heappush(pq, (-nextTop, count))
            
                        
        return res % M
```


