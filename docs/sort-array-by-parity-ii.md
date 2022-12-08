---
id: sort-array-by-parity-ii
title: Sort Array By Parity II
description: Problem Description and Solution for Sort Array By Parity II
sidebar_label: 922. Sort Array By Parity II
sidebar_position: 922
---

# [922. Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)

```py title=sort-array-by-parity-ii.py
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, 1
        
        while i < n and j < n:
            while i < n and nums[i] & 1 == 0:
                i += 2
            
            while j < n and nums[j] & 1:
                j += 2
            
            if i < n and j < n:
                nums[i], nums[j] = nums[j], nums[i]
        
        return nums
```


