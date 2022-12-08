---
id: array-of-doubled-pairs
title: Array of Doubled Pairs
description: Problem Description and Solution for Array of Doubled Pairs
sidebar_label: 954. Array of Doubled Pairs
sidebar_position: 954
---

# [954. Array of Doubled Pairs](https://leetcode.com/problems/array-of-doubled-pairs/)

```py title=array-of-doubled-pairs.py
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = collections.Counter(arr)
        arr.sort()
        
        for x in arr:
            if counter[x] == 0: continue
            
            if x < 0 and x & 1: return False
            
            t = x * 2 if x > 0 else x // 2
            
            if counter[t] == 0: return False
            
            counter[x] -= 1
            counter[t] -= 1
        
        return True
```


