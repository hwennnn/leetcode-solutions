---
id: minimum-interval-to-include-each-query
title: Minimum Interval to Include Each Query
description: Problem Description and Solution for Minimum Interval to Include Each Query
sidebar_label: 1851. Minimum Interval to Include Each Query
sidebar_position: 1851
---

# [1851. Minimum Interval to Include Each Query](https://leetcode.com/problems/minimum-interval-to-include-each-query/)

```py title=minimum-interval-to-include-each-query.py
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        A = sorted(intervals)[::-1]
        pq = []
        res = {}
        
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                
                if j >= q:
                    heapq.heappush(pq, [j - i + 1, j])
            
            while pq and pq[0][1] < q:
                heapq.heappop(pq)
            
            res[q] = pq[0][0] if pq else -1
        
        return [res[q] for q in queries]
```


