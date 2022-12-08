---
id: contains-duplicate
title: Contains Duplicate
description: Problem Description and Solution for Contains Duplicate
sidebar_label: 217. Contains Duplicate
sidebar_position: 217
---

# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)

```py title=contains-duplicate.py
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        
        for x in nums:
            if x in s: return True
            s.add(x)
        
        return False
```


