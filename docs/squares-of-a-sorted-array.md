---
id: squares-of-a-sorted-array
title: Squares of a Sorted Array
description: Problem Description and Solution for Squares of a Sorted Array
sidebar_label: 977. Squares of a Sorted Array
sidebar_position: 977
---

# [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

```py title=squares-of-a-sorted-array.py
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        i, j, p = 0, n - 1, n - 1
        
        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                res[p] = nums[i] * nums[i]
                i += 1
            else:
                res[p] = nums[j] * nums[j]
                j -= 1
            
            p -= 1
        
        return res
```


