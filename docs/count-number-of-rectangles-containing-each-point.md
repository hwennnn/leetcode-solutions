---
id: count-number-of-rectangles-containing-each-point
title: Count Number of Rectangles Containing Each Point
description: Problem Description and Solution for Count Number of Rectangles Containing Each Point
sidebar_label: 2250. Count Number of Rectangles Containing Each Point
sidebar_position: 2250
---

# [2250. Count Number of Rectangles Containing Each Point](https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/)

```py title=count-number-of-rectangles-containing-each-point.py
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        n = len(rectangles)
        res = []
        mp = defaultdict(list)

        for x, y in rectangles:
            mp[y].append(x)
        
        for k, v in mp.items():
            v.sort()
        
        for x, y in points:
            count = 0
            
            for z in range(y, 101):
                l = mp[z]
                
                xIndex = bisect.bisect_left(l, x)

                count += len(l) - xIndex
                    
            res.append(count)
        
        return res
```


