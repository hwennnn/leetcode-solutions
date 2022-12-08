---
id: water-bottles
title: Water Bottles
description: Problem Description and Solution for Water Bottles
sidebar_label: 1518. Water Bottles
sidebar_position: 1518
---

# [1518. Water Bottles](https://leetcode.com/problems/water-bottles/)

```py title=water-bottles.py
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        while numBottles >= numExchange:
            remain = numBottles%numExchange
            numBottles //= numExchange
            res += numBottles
            numBottles += remain

        return res
           
```

```cpp title=water-bottles.cpp
class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        int res = numBottles;
        
        while (numBottles >= numExchange){
            int remaining = numBottles % numExchange;
            numBottles /= numExchange;
            res += numBottles;
            numBottles += remaining;
        }
           
        return res;
        
    }
};
```


