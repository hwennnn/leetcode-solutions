---
id: maximum-total-importance-of-roads
title: Maximum Total Importance of Roads
description: Problem Description and Solution for Maximum Total Importance of Roads
sidebar_label: 2285. Maximum Total Importance of Roads
sidebar_position: 2285
---

# [2285. Maximum Total Importance of Roads](https://leetcode.com/problems/maximum-total-importance-of-roads/)

```py title=maximum-total-importance-of-roads.py
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = defaultdict(int)

        for a, b in roads:
            count[a] += 1
            count[b] += 1

        scores = defaultdict(int)
        
        v = sorted(count.items(), key = lambda x:-x[1])
        
        for k, cnt in v:
            scores[k] = n
            n -= 1
        
        res = 0
        
        for a, b in roads:
            res += scores[a] + scores[b]
        
        return res
```


