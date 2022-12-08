---
id: merge-triplets-to-form-target-triplet
title: Merge Triplets to Form Target Triplet
description: Problem Description and Solution for Merge Triplets to Form Target Triplet
sidebar_label: 1899. Merge Triplets to Form Target Triplet
sidebar_position: 1899
---

# [1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/)

```py title=merge-triplets-to-form-target-triplet.py
class Solution:
    def mergeTriplets(self, t: List[List[int]], target: List[int]) -> bool:
        res = [False] * 3
        
        for a,b,c in t:            
            if a == target[0] and b <= target[1] and c <= target[2]: 
                res[0] = True
            if b == target[1] and a <= target[0] and c <= target[2]: 
                res[1] = True
            if c == target[2] and b <= target[1] and a <= target[0]: 
                res[2] = True
                
        return all(res)
```


