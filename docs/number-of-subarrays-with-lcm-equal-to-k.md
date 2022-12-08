---
id: number-of-subarrays-with-lcm-equal-to-k
title: Number of Subarrays With LCM Equal to K
description: Problem Description and Solution for Number of Subarrays With LCM Equal to K
sidebar_label: 2470. Number of Subarrays With LCM Equal to K
sidebar_position: 2470
---

# [2470. Number of Subarrays With LCM Equal to K](https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/)

```py title=number-of-subarrays-with-lcm-equal-to-k.py
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        
        for i in range(N):
            l = nums[i]
            
            for j in range(i, N):
                l = lcm(l, nums[j])
                
                if l > k: break
                
                if l == k:
                    res += 1
        
        return res
                
        
        
```


