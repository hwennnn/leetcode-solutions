---
id: display-table-of-food-orders-in-a-restaurant
title: Display Table of Food Orders in a Restaurant
description: Problem Description and Solution for Display Table of Food Orders in a Restaurant
sidebar_label: 1418. Display Table of Food Orders in a Restaurant
sidebar_position: 1418
---

# [1418. Display Table of Food Orders in a Restaurant](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/)

```py title=display-table-of-food-orders-in-a-restaurant.py
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foodset = set()
        tablemp = collections.defaultdict(map)
        
        for _, t, f in orders:
            foodset.add(f)
            if t not in tablemp:
                tablemp[t] = collections.defaultdict(int)
            tablemp[t][f] += 1

        res = [["Table"]]
        
        S = sorted(list(foodset))
        for s in S:
            res[0].append(s)
        
        tablelist = []
        
        for t in tablemp:
            tmp = [t]
            foods = tablemp[t]
            
            for f in res[0][1:]:
                if f not in foods:
                    tmp.append("0")
                else:
                    tmp.append(str(foods[f]))
                    
            tablelist.append(tmp)
            
        tablelist.sort(key = lambda x : int(x[0]))
        
        return res + tablelist
```


