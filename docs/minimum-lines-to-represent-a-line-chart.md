---
id: minimum-lines-to-represent-a-line-chart
title: Minimum Lines to Represent a Line Chart
description: Problem Description and Solution for Minimum Lines to Represent a Line Chart
sidebar_label: 2280. Minimum Lines to Represent a Line Chart
sidebar_position: 2280
---

# [2280. Minimum Lines to Represent a Line Chart](https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/)

```py title=minimum-lines-to-represent-a-line-chart.py
class Solution:
    def minimumLines(self, stock: List[List[int]]) -> int:
        n = len(stock)
        
        if n == 1: return 0
        
        stock.sort(key = lambda x: x[0])
        dx = stock[0][0] - stock[1][0]
        dy = stock[0][1] - stock[1][1]
            
        res = 1
        
        for index in range(2, n):
            x, y = stock[index]
        
            dx1 = stock[index - 1][0] - stock[index][0]
            dy1 = stock[index - 1][1] - stock[index][1]  
            
            if dx1 * dy != dx * dy1:
                res += 1
                dx = dx1
                dy = dy1
        
        return res
```


