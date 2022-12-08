---
id: remove-stones-to-minimize-the-total
title: Remove Stones to Minimize the Total
description: Problem Description and Solution for Remove Stones to Minimize the Total
sidebar_label: 1962. Remove Stones to Minimize the Total
sidebar_position: 1962
---

# [1962. Remove Stones to Minimize the Total](https://leetcode.com/problems/remove-stones-to-minimize-the-total/)

```py title=remove-stones-to-minimize-the-total.py
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap)
        
        res = 0
        for _ in range(k):
            pile = -heapq.heappop(heap)
            res += pile
            heapq.heappush(heap, -ceil(pile / 2))
        
        return -sum(heap)
        
```


