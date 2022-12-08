---
id: minimum-fuel-cost-to-report-to-the-capital
title: Minimum Fuel Cost to Report to the Capital
description: Problem Description and Solution for Minimum Fuel Cost to Report to the Capital
sidebar_label: 2477. Minimum Fuel Cost to Report to the Capital
sidebar_position: 2477
---

# [2477. Minimum Fuel Cost to Report to the Capital](https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/)

```py title=minimum-fuel-cost-to-report-to-the-capital.py
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        N = len(roads)
        res = 0
        graph = defaultdict(list)

        for x, y in roads:
            graph[x].append(y)
            graph[y].append(x)
        
        def go(node, prev):
            nonlocal res

            people = 1

            for nei in graph[node]:
                if nei != prev:
                    people += go(nei, node)
            
            if node != 0:
                res += ceil(people / seats)
            
            return people

        go(0, 0)
        return res
```


