---
id: peak-index-in-a-mountain-array
title: Peak Index in a Mountain Array
description: Problem Description and Solution for Peak Index in a Mountain Array
sidebar_label: 852. Peak Index in a Mountain Array
sidebar_position: 852
---

# [852. Peak Index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/)

```py title=peak-index-in-a-mountain-array.py
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        low, high = 0, len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] < arr[mid+1]:
                low = mid + 1
            
            elif arr[mid-1] > arr[mid]:
                high = mid - 1
            
            else:
                return mid
        
        return -1
```


