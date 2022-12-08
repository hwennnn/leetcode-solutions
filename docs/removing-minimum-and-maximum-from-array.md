---
id: removing-minimum-and-maximum-from-array
title: Removing Minimum and Maximum From Array
description: Problem Description and Solution for Removing Minimum and Maximum From Array
sidebar_label: 2091. Removing Minimum and Maximum From Array
sidebar_position: 2091
---

# [2091. Removing Minimum and Maximum From Array](https://leetcode.com/problems/removing-minimum-and-maximum-from-array/)

```py title=removing-minimum-and-maximum-from-array.py
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        mmax, mmin = float('-inf'), float('inf')
        maxi = mini = -1
        
        for i, x in enumerate(nums):
            if x > mmax:
                mmax, maxi = x, i
                
            if x < mmin:
                mmin, mini = x, i
            
        removeFromLeft = max(mini, maxi) + 1
        removeFromRight = n - min(mini, maxi)
        removeFromLeftAndRight = (min(mini, maxi) + 1) + (n - max(mini, maxi))
        
        return min(removeFromLeft, removeFromRight, removeFromLeftAndRight)
```


