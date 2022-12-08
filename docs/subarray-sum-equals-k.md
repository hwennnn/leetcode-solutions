---
id: subarray-sum-equals-k
title: Subarray Sum Equals K
description: Problem Description and Solution for Subarray Sum Equals K
sidebar_label: 560. Subarray Sum Equals K
sidebar_position: 560
---

# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

```py title=subarray-sum-equals-k.py
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        
        s = res = 0
        
        for x in nums:
            s += x
            
            if s - k in mp:
                res += mp[s - k]
            
            mp[s] += 1
        
        return res
```


