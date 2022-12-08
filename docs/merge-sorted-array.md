---
id: merge-sorted-array
title: Merge Sorted Array
description: Problem Description and Solution for Merge Sorted Array
sidebar_label: 88. Merge Sorted Array
sidebar_position: 88
---

# [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)

```py title=merge-sorted-array.py
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n - 1
        m -= 1
        n -= 1
        
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m -= 1
            else:
                nums1[index] = nums2[n]
                n -= 1
                
            index -= 1
        
        while m >= 0:
            nums1[index] = nums1[m]
            m -= 1
            index -= 1
        
        while n >= 0:
            nums1[index] = nums2[n]
            n -= 1
            index -= 1
        
        return nums1
```


