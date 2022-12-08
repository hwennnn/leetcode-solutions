---
id: poor-pigs
title: Poor Pigs
description: Problem Description and Solution for Poor Pigs
sidebar_label: 458. Poor Pigs
sidebar_position: 458
---

# [458. Poor Pigs](https://leetcode.com/problems/poor-pigs/)

```py title=poor-pigs.py
class Solution:
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
```


