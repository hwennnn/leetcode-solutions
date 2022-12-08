---
id: create-target-array-in-the-given-order
title: Create Target Array in the Given Order
description: Problem Description and Solution for Create Target Array in the Given Order
sidebar_label: 1389. Create Target Array in the Given Order
sidebar_position: 1389
---

# [1389. Create Target Array in the Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/)

```py title=create-target-array-in-the-given-order.py
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        res = []
        for n,i in zip(nums,index):
            res.insert(i,n)
        
        return res
```


