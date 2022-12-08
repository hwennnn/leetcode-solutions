---
id: partition-array-into-three-parts-with-equal-sum
title: Partition Array Into Three Parts With Equal Sum
description: Problem Description and Solution for Partition Array Into Three Parts With Equal Sum
sidebar_label: 1013. Partition Array Into Three Parts With Equal Sum
sidebar_position: 1013
---

# [1013. Partition Array Into Three Parts With Equal Sum](https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/)

```py title=partition-array-into-three-parts-with-equal-sum.py
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)
        if total % 3 != 0: return False
        target = total // 3
        count = s = 0
        
        for i, x in enumerate(arr):
            s += x
            
            if s == target:
                s = 0
                count += 1
        
        return count >= 3
```


