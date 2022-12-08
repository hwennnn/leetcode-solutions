---
id: find-in-mountain-array
title: Find in Mountain Array
description: Problem Description and Solution for Find in Mountain Array
sidebar_label: 1095. Find in Mountain Array
sidebar_position: 1095
---

# [1095. Find in Mountain Array](https://leetcode.com/problems/find-in-mountain-array/)

```py title=find-in-mountain-array.py
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length();
        peak = 0
        
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
        peak = left
        
        left, right = 0, peak
        while left <= right:
            mid = (left + right) >> 1
            
            if mountain_arr.get(mid) > target:
                right = mid - 1
            elif mountain_arr.get(mid) < target:
                left = mid + 1
            else:
                return mid
        
        left, right = peak, n - 1
        while left <= right:
            mid = (left + right) >> 1
            
            if mountain_arr.get(mid) < target:
                right = mid - 1
            elif mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                return mid
        
        return -1
        
        
```


