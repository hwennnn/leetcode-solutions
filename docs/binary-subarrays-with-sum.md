---
id: binary-subarrays-with-sum
title: Binary Subarrays With Sum
description: Problem Description and Solution for Binary Subarrays With Sum
sidebar_label: 930. Binary Subarrays With Sum
sidebar_position: 930
---

# [930. Binary Subarrays With Sum](https://leetcode.com/problems/binary-subarrays-with-sum/)

```py title=binary-subarrays-with-sum.py
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = Counter()
        count[0] = 1
        res = s = 0
        
        for x in nums:
            s += x
            
            res += count[s - goal]
            
            count[s] += 1
    
        return res
```


