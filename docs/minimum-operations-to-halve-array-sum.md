---
id: minimum-operations-to-halve-array-sum
title: Minimum Operations to Halve Array Sum
description: Problem Description and Solution for Minimum Operations to Halve Array Sum
sidebar_label: 2208. Minimum Operations to Halve Array Sum
sidebar_position: 2208
---

# [2208. Minimum Operations to Halve Array Sum](https://leetcode.com/problems/minimum-operations-to-halve-array-sum/)

```py title=minimum-operations-to-halve-array-sum.py
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total = sum(nums)
        target = total / 2
        res = 0
        
        pq = [-x for x in nums]
        heapq.heapify(pq)
        
        while total > target:
            x = heapq.heappop(pq)
            x = (-x) / 2
            
            total -= x
            res += 1
            
            heapq.heappush(pq, -x)
        
        return res
        
```


