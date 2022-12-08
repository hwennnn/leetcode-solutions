---
id: maximum-number-of-non-overlapping-subarrays-with-sum-equals-target
title: Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
description: Problem Description and Solution for Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
sidebar_label: 1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
sidebar_position: 1546
---

# [1546. Maximum Number of Non-Overlapping Subarrays With Sum Equals Target](https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/)

```py title=maximum-number-of-non-overlapping-subarrays-with-sum-equals-target.py
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        
        d = {0:-1}
        last = -1
        s = res = 0
        
        for i,num in enumerate(nums):
            s += num
            if s - target in d and d[s-target] >= last:
                last = i
                res += 1
            
            d[s] = i
        
        return res
```


