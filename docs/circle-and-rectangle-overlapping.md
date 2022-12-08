---
id: circle-and-rectangle-overlapping
title: Circle and Rectangle Overlapping
description: Problem Description and Solution for Circle and Rectangle Overlapping
sidebar_label: 1401. Circle and Rectangle Overlapping
sidebar_position: 1401
---

# [1401. Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/)

```cpp title=circle-and-rectangle-overlapping.cpp
class Solution {
public:
    bool checkOverlap(int radius, int x_center, int y_center, int x1, int y1, int x2, int y2) {
        x1 -= x_center, x2 -= x_center;
        y1 -= y_center, y2 -= y_center;
        
        int minX = x1 * x2 > 0 ? min(x1*x1, x2*x2) : 0;
        int minY = y1 * y2 > 0 ? min(y1*y1, y2*y2) : 0;
        
        return minX + minY <= radius * radius;
    }
};
```


