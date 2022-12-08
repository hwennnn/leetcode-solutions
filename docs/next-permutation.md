---
id: next-permutation
title: Next Permutation
description: Problem Description and Solution for Next Permutation
sidebar_label: 31. Next Permutation
sidebar_position: 31
---

# [31. Next Permutation](https://leetcode.com/problems/next-permutation/)

```py title=next-permutation.py
class Solution:
    def nextPermutation(self, nums):
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:   # nums are in descending order
            nums.reverse()
            return 
        k = i - 1    # find the last "ascending" position
        while nums[j] <= nums[k]:
            j -= 1
        nums[k], nums[j] = nums[j], nums[k]  
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l +=1 ; r -= 1
```


