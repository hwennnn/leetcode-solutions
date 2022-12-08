---
id: move-zeroes
title: Move Zeroes
description: Problem Description and Solution for Move Zeroes
sidebar_label: 283. Move Zeroes
sidebar_position: 283
---

# [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

```py title=move-zeroes.py
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPos = 0
        
        for i, x in enumerate(nums):
            if x != 0:
                nums[i], nums[zeroPos] = nums[zeroPos], nums[i]
                zeroPos += 1
```


