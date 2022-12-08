---
id: minimum-difference-in-sums-after-removal-of-elements
title: Minimum Difference in Sums After Removal of Elements
description: Problem Description and Solution for Minimum Difference in Sums After Removal of Elements
sidebar_label: 2163. Minimum Difference in Sums After Removal of Elements
sidebar_position: 2163
---

# [2163. Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/)

```py title=minimum-difference-in-sums-after-removal-of-elements.py
from sortedcontainers import SortedList

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3
        
        left = SortedList(nums[:n])
        right = SortedList(nums[n:])
        sumLeft = sum(left)
        sumRight = sum(right[-n:])
        res = sumLeft - sumRight
        
        for i in range(n, 2 * n):
            index = right.bisect_left(nums[i])
            
            if index >= len(right) - n:
                sumRight -= nums[i]
                sumRight += right[-n-1]
            
            index = left.bisect_left(nums[i])
            
            if index < n:
                sumLeft += nums[i]
                sumLeft -= left[n - 1]
            
            right.discard(nums[i])
            left.add(nums[i])
            
            res = min(res, sumLeft - sumRight)
        
        return res
        
```


