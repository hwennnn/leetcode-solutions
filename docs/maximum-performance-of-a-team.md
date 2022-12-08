---
id: maximum-performance-of-a-team
title: Maximum Performance of a Team
description: Problem Description and Solution for Maximum Performance of a Team
sidebar_label: 1383. Maximum Performance of a Team
sidebar_position: 1383
---

# [1383. Maximum Performance of a Team](https://leetcode.com/problems/maximum-performance-of-a-team/)

```py title=maximum-performance-of-a-team.py
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        M = 10 ** 9 + 7
        heap = []
        res = currSpeed = 0
        
        for e, s in sorted(zip(efficiency, speed), reverse = 1):
            currSpeed += s
            heappush(heap, s)
            
            if len(heap) > k:
                currSpeed -= heappop(heap)
            
            res = max(res, e * currSpeed)
            
        return res % M
        
```


