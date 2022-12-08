---
id: kth-missing-positive-number
title: Kth Missing Positive Number
description: Problem Description and Solution for Kth Missing Positive Number
sidebar_label: 1539. Kth Missing Positive Number
sidebar_position: 1539
---

# [1539. Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)

```py title=kth-missing-positive-number.py
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        start = 1
        
        s = set(arr)
        
        while k > 0 and start <= 1000:
            if start not in s: k -= 1
                
            start += 1
        
        if k > 0: start += k
        
        return start - 1
        
```


