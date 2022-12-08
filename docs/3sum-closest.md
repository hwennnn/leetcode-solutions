---
id: 3sum-closest
title: 3Sum Closest
description: Problem Description and Solution for 3Sum Closest
sidebar_label: 16. 3Sum Closest
sidebar_position: 16
---

# [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

```py title=3sum-closest.py
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = nums[0] + nums[1] + nums[-1]
        nums.sort()
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                
                if s == target:
                    return s
                elif s > target:
                    k -= 1
                else:
                    j += 1
                
                if abs(s - target) < abs(res - target):
                    res = s
        
        return res
```


