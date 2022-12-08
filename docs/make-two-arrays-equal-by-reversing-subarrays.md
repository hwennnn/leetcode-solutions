---
id: make-two-arrays-equal-by-reversing-subarrays
title: Make Two Arrays Equal by Reversing Subarrays
description: Problem Description and Solution for Make Two Arrays Equal by Reversing Subarrays
sidebar_label: 1460. Make Two Arrays Equal by Reversing Subarrays
sidebar_position: 1460
---

# [1460. Make Two Arrays Equal by Reversing Subarrays](https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/)

```py title=make-two-arrays-equal-by-reversing-subarrays.py
class Solution:
    def canBeEqual(self, target: List[int], lst: List[int]) -> bool:
        
        n = 1001
        arr = [0]*n
        
        for i in range(len(target)):
            arr[target[i]] += 1
            arr[lst[i]] -= 1
        
        for i in range(n):   
            if arr[i] != 0:
                return False
        
        return True
        
        
```


