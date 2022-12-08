---
id: k-closest-points-to-origin
title: K Closest Points to Origin
description: Problem Description and Solution for K Closest Points to Origin
sidebar_label: 973. K Closest Points to Origin
sidebar_position: 973
---

# [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

```py title=k-closest-points-to-origin.py
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        
        for x, y in points:
            if len(pq) == k:
                heapq.heappushpop(pq, (-(x * x + y * y), x, y))
            else:
                heapq.heappush(pq, (-(x * x + y * y), x, y))
                
        return [[x, y] for _, x, y in pq]
```


