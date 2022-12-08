---
id: circular-permutation-in-binary-representation
title: Circular Permutation in Binary Representation
description: Problem Description and Solution for Circular Permutation in Binary Representation
sidebar_label: 1238. Circular Permutation in Binary Representation
sidebar_position: 1238
---

# [1238. Circular Permutation in Binary Representation](https://leetcode.com/problems/circular-permutation-in-binary-representation/)

```py title=circular-permutation-in-binary-representation.py
class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        
        for i in range(1 << n):
            res.append(i ^ i >> 1)
        
        i = res.index(start)
        return res[i:] + res[:i]

            

```


