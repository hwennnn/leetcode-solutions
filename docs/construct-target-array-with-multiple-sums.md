---
id: construct-target-array-with-multiple-sums
title: Construct Target Array With Multiple Sums
description: Problem Description and Solution for Construct Target Array With Multiple Sums
sidebar_label: 1354. Construct Target Array With Multiple Sums
sidebar_position: 1354
---

# [1354. Construct Target Array With Multiple Sums](https://leetcode.com/problems/construct-target-array-with-multiple-sums/)

```py title=construct-target-array-with-multiple-sums.py
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapify(heap)
        
        while True:
            x = -heappop(heap)
            total -= x
            
            if x == 1 or total == 1: return True
            
            if x < total or total == 0 or x % total == 0: return False
            
            x %= total
            total += x
            
            heappush(heap, -x)
```


