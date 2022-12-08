---
id: remove-duplicates-from-sorted-array-ii
title: Remove Duplicates from Sorted Array II
description: Problem Description and Solution for Remove Duplicates from Sorted Array II
sidebar_label: 80. Remove Duplicates from Sorted Array II
sidebar_position: 80
---

# [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

```py title=remove-duplicates-from-sorted-array-ii.py
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        
        return i
            
```


