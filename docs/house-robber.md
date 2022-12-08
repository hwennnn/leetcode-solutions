---
id: house-robber
title: House Robber
description: Problem Description and Solution for House Robber
sidebar_label: 198. House Robber
sidebar_position: 198
---

# [198. House Robber](https://leetcode.com/problems/house-robber/)

```py title=house-robber.py
class Solution:
    def rob(self, nums: List[int]) -> int:
        take = skip = 0
        
        for x in nums:
            take, skip = max(take, skip + x), max(skip, take)
            
        return take
```


