---
id: gas-station
title: Gas Station
description: Problem Description and Solution for Gas Station
sidebar_label: 134. Gas Station
sidebar_position: 134
---

# [134. Gas Station](https://leetcode.com/problems/gas-station/)

```py title=gas-station.py
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        
        start = tank = 0
        
        for end in range(n * 2):
            if tank < 0:
                start = end
                tank = 0
            
            tank += gas[end % n] - cost[end % n]
            
        return start if start < n else -1
        
        
```


