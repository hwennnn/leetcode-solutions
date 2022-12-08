---
id: find-k-closest-elements
title: Find K Closest Elements
description: Problem Description and Solution for Find K Closest Elements
sidebar_label: 658. Find K Closest Elements
sidebar_position: 658
---

# [658. Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)

```py title=find-k-closest-elements.py
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        pq = []

        for i, num in enumerate(arr):
            d = abs(num - x)
            if len(pq) == k:
                heappushpop(pq, (-d, -i))
            else:
                heappush(pq, (-d, -i))
        
        res = []

        while pq:
            d, index = heappop(pq)
            index = -index
            res.append(arr[index])

        return sorted(res)
            
```


