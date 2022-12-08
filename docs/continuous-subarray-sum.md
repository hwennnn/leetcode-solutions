---
id: continuous-subarray-sum
title: Continuous Subarray Sum
description: Problem Description and Solution for Continuous Subarray Sum
sidebar_label: 523. Continuous Subarray Sum
sidebar_position: 523
---

# [523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

```py title=continuous-subarray-sum.py
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0:-1}
        s = 0
        
        for i, x in enumerate(nums):
            s = (s + x) % k
            if s not in mp:
                mp[s] = i
            
            if i - mp[s] >= 2:
                return True
        
        return False
```


