---
id: maximum-product-after-k-increments
title: Maximum Product After K Increments
description: Problem Description and Solution for Maximum Product After K Increments
sidebar_label: 2233. Maximum Product After K Increments
sidebar_position: 2233
---

# [2233. Maximum Product After K Increments](https://leetcode.com/problems/maximum-product-after-k-increments/)

```py title=maximum-product-after-k-increments.py
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        pq = [x for x in nums]
        heapq.heapify(pq)
        
        while k > 0:
            x = heapq.heappop(pq) + 1
            heapq.heappush(pq, x)
            k -= 1
        
        x = 1
        
        for y in pq:
            x *= y
            x %= M

        return x
        
```


