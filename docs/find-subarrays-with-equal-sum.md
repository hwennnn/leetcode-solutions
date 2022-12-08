---
id: find-subarrays-with-equal-sum
title: Find Subarrays With Equal Sum
description: Problem Description and Solution for Find Subarrays With Equal Sum
sidebar_label: 2395. Find Subarrays With Equal Sum
sidebar_position: 2395
---

# [2395. Find Subarrays With Equal Sum](https://leetcode.com/problems/find-subarrays-with-equal-sum/)

```py title=find-subarrays-with-equal-sum.py
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        n = len(nums)
        
        seen = set()
        
        for i in range(n - 1):
            curr = nums[i] + nums[i + 1]
            
            if curr in seen:
                return True
            
            seen.add(curr)
        
        return False
                
```


