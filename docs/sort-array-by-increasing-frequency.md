---
id: sort-array-by-increasing-frequency
title: Sort Array by Increasing Frequency
description: Problem Description and Solution for Sort Array by Increasing Frequency
sidebar_label: 1636. Sort Array by Increasing Frequency
sidebar_position: 1636
---

# [1636. Sort Array by Increasing Frequency](https://leetcode.com/problems/sort-array-by-increasing-frequency/)

```py title=sort-array-by-increasing-frequency.py
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        c = sorted(c.items(), key = lambda x : (x[1],-x[0]))

        res = []
        
        for key,value in c:
            for _ in range(value):
                res.append(key)
        
        return res
```


