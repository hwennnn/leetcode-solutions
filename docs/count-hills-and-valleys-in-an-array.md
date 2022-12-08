---
id: count-hills-and-valleys-in-an-array
title: Count Hills and Valleys in an Array
description: Problem Description and Solution for Count Hills and Valleys in an Array
sidebar_label: 2210. Count Hills and Valleys in an Array
sidebar_position: 2210
---

# [2210. Count Hills and Valleys in an Array](https://leetcode.com/problems/count-hills-and-valleys-in-an-array/)

```py title=count-hills-and-valleys-in-an-array.py
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        
        for i in range(1, n - 1):
            if nums[i] == nums[i + 1]: continue
            left = i - 1
            right = i + 1
            
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            
            while right < n and nums[right] == nums[i]:
                right += 1
            
            if left >= 0 and right < n:
                l, r = nums[left], nums[right]
                if (nums[i] > l and nums[i] > r) or (nums[i] < l and nums[i] < r):
                    res += 1
        
        return res
```


