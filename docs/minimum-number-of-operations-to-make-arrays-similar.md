---
id: minimum-number-of-operations-to-make-arrays-similar
title: Minimum Number of Operations to Make Arrays Similar
description: Problem Description and Solution for Minimum Number of Operations to Make Arrays Similar
sidebar_label: 2449. Minimum Number of Operations to Make Arrays Similar
sidebar_position: 2449
---

# [2449. Minimum Number of Operations to Make Arrays Similar](https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/)

```py title=minimum-number-of-operations-to-make-arrays-similar.py
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        A = sorted(nums, key = lambda x : (x & 1, x))
        B = sorted(target, key = lambda x : (x & 1, x))
        res = 0
        
        for a, b in zip(A, B):
            if a > b:
                res += a - b

        return res // 2
```


