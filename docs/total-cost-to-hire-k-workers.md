---
id: total-cost-to-hire-k-workers
title: Total Cost to Hire K Workers
description: Problem Description and Solution for Total Cost to Hire K Workers
sidebar_label: 2462. Total Cost to Hire K Workers
sidebar_position: 2462
---

# [2462. Total Cost to Hire K Workers](https://leetcode.com/problems/total-cost-to-hire-k-workers/)

```py title=total-cost-to-hire-k-workers.py
class Solution:
    def totalCost(self, costs: List[int], k: int, C: int) -> int:
        N = len(costs)
        left = []
        right = []
        res = 0
        i, j = 0, N - 1

        for _ in range(k):
            while len(left) < C and i <= j:
                heappush(left, (costs[i], i))
                i += 1
            
            while len(right) < C and j >= i:
                heappush(right, (costs[j], j))
                j -= 1
                
            lx, li = left[0] if len(left) > 0 else (inf, -1)
            rx, ri = right[0] if len(right) > 0 else (inf, -1)

            if len(right) == 0 or lx <= rx:
                res += lx
                heappop(left)
            else:
                res += rx
                heappop(right)
        
        return res
```


