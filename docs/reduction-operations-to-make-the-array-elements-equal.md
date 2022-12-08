---
id: reduction-operations-to-make-the-array-elements-equal
title: Reduction Operations to Make the Array Elements Equal
description: Problem Description and Solution for Reduction Operations to Make the Array Elements Equal
sidebar_label: 1887. Reduction Operations to Make the Array Elements Equal
sidebar_position: 1887
---

# [1887. Reduction Operations to Make the Array Elements Equal](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/)

```py title=reduction-operations-to-make-the-array-elements-equal.py
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        keys = sorted(counter.keys(), reverse = 1)
        
        curr = res = 0
        for key in keys[:-1]:
            curr += counter[key]
            res += curr
        
        return res
```


