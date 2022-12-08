---
id: best-sightseeing-pair
title: Best Sightseeing Pair
description: Problem Description and Solution for Best Sightseeing Pair
sidebar_label: 1014. Best Sightseeing Pair
sidebar_position: 1014
---

# [1014. Best Sightseeing Pair](https://leetcode.com/problems/best-sightseeing-pair/)

```py title=best-sightseeing-pair.py
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = curr = 0
        
        for v in values:
            res = max(res, curr + v)
            curr = max(curr, v) - 1
        
        return res
```


