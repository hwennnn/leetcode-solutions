---
id: last-stone-weight
title: Last Stone Weight
description: Problem Description and Solution for Last Stone Weight
sidebar_label: 1046. Last Stone Weight
sidebar_position: 1046
---

# [1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

```py title=last-stone-weight.py
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)
        
        while len(heap) >= 2:
            y, x = -heapq.heappop(heap), -heapq.heappop(heap)
            
            if x != y:
                heapq.heappush(heap, -(y - x))
        
        return -heap[0] if heap else 0
```


