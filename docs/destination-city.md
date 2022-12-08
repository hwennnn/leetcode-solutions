---
id: destination-city
title: Destination City
description: Problem Description and Solution for Destination City
sidebar_label: 1436. Destination City
sidebar_position: 1436
---

# [1436. Destination City](https://leetcode.com/problems/destination-city/)

```py title=destination-city.py
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        mp = collections.defaultdict(int)
        
        for a, b in paths:
            mp[a] += 1
            mp[b] += 1
        
        for a,b in paths:
            if mp[b] == 1:
                return b
```


