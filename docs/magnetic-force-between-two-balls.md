---
id: magnetic-force-between-two-balls
title: Magnetic Force Between Two Balls
description: Problem Description and Solution for Magnetic Force Between Two Balls
sidebar_label: 1552. Magnetic Force Between Two Balls
sidebar_position: 1552
---

# [1552. Magnetic Force Between Two Balls](https://leetcode.com/problems/magnetic-force-between-two-balls/)

```py title=magnetic-force-between-two-balls.py
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()
        
        def count(d):
            ans, curr = 1, position[0]
            
            for i in range(1,n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            
            return ans
        
        l, r = 0, position[-1] - position[0]
        
        while l < r:
            mid = r - (r-l) // 2
            
            if count(mid) >= m:
                l = mid
        
            else:
                r = mid-1
        
        return l
            
```


