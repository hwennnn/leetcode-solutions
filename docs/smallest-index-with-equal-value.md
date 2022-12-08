---
id: smallest-index-with-equal-value
title: Smallest Index With Equal Value
description: Problem Description and Solution for Smallest Index With Equal Value
sidebar_label: 2057. Smallest Index With Equal Value
sidebar_position: 2057
---

# [2057. Smallest Index With Equal Value](https://leetcode.com/problems/smallest-index-with-equal-value/)

```py title=smallest-index-with-equal-value.py
class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            if i % 10 == x:
                return i
            
        return -1
```


