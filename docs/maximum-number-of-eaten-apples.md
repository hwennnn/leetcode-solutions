---
id: maximum-number-of-eaten-apples
title: Maximum Number of Eaten Apples
description: Problem Description and Solution for Maximum Number of Eaten Apples
sidebar_label: 1705. Maximum Number of Eaten Apples
sidebar_position: 1705
---

# [1705. Maximum Number of Eaten Apples](https://leetcode.com/problems/maximum-number-of-eaten-apples/)

```py title=maximum-number-of-eaten-apples.py
from heapq import heappop, heappush
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        i = res = 0
        
        heap = []
        
        while True:
            if i < n:
                heappush(heap, (days[i] + i, apples[i]))
            
            while heap and i >= heap[0][0]:
                heappop(heap)
                
            if heap:
                rot, apple = heappop(heap)
                res += 1
                if apple > 1:
                    heappush(heap, (rot, apple - 1))
            
            
            if not heap and i >= n: break
            
            i += 1
        
        return res
```


