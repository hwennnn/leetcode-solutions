---
id: diagonal-traverse-ii
title: Diagonal Traverse II
description: Problem Description and Solution for Diagonal Traverse II
sidebar_label: 1424. Diagonal Traverse II
sidebar_position: 1424
---

# [1424. Diagonal Traverse II](https://leetcode.com/problems/diagonal-traverse-ii/)

```py title=diagonal-traverse-ii.py
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        
        mp = collections.defaultdict(list)
        
        for i, r in enumerate(nums):
            for j,v in enumerate(r):
                mp[i+j].append(v)
                
        return [v for key in mp for v in mp[key][::-1] ]
        
```


