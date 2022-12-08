---
id: minimum-elements-to-add-to-form-a-given-sum
title: Minimum Elements to Add to Form a Given Sum
description: Problem Description and Solution for Minimum Elements to Add to Form a Given Sum
sidebar_label: 1785. Minimum Elements to Add to Form a Given Sum
sidebar_position: 1785
---

# [1785. Minimum Elements to Add to Form a Given Sum](https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/)

```py title=minimum-elements-to-add-to-form-a-given-sum.py
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        total = sum(nums)
        target = abs(goal - total)
        
        res = target // limit + (1 if target % limit else 0)
        
        return res
```


