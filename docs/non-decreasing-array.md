---
id: non-decreasing-array
title: Non-decreasing Array
description: Problem Description and Solution for Non-decreasing Array
sidebar_label: 665. Non-decreasing Array
sidebar_position: 665
---

# [665. Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/)

```py title=non-decreasing-array.py
class Solution:
    def checkPossibility(self, nums):

        if len(nums) < 3: return True
        
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                count += 1
                if count > 1:
                    return False
                if i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                
        return count <= 1
```


