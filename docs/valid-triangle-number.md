---
id: valid-triangle-number
title: Valid Triangle Number
description: Problem Description and Solution for Valid Triangle Number
sidebar_label: 611. Valid Triangle Number
sidebar_position: 611
---

# [611. Valid Triangle Number](https://leetcode.com/problems/valid-triangle-number/)

```py title=valid-triangle-number.py
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        
        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i
                    j -= 1
                else:
                    i += 1
        
        return res
            
                
```


