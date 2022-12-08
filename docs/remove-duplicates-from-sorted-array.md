---
id: remove-duplicates-from-sorted-array
title: Remove Duplicates from Sorted Array
description: Problem Description and Solution for Remove Duplicates from Sorted Array
sidebar_label: 26. Remove Duplicates from Sorted Array
sidebar_position: 26
---

# [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

```py title=remove-duplicates-from-sorted-array.py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        for num in nums:
            if i == 0 or num > nums[i-1]:
                nums[i] = num
                i += 1
        
        return i
```


